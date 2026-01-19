let employeeList = JSON.parse(localStorage.getItem("empData")) || [];
let editEmpIndex = null;

function saveEmployee() {
    const emp = {
        id: empId.value,
        name: empName.value,
        dept: empDept.value,
        email: empEmail.value,
        salary: empSalary.value
    };

    if (!emp.id || !emp.name || !emp.dept || !emp.email || !emp.salary) {
        alert("All fields are required");
        return;
    }

    if (editEmpIndex === null) {
        employeeList.push(emp);
    } else {
        employeeList[editEmpIndex] = emp;
        editEmpIndex = null;
        btnSave.innerText = "Save Employee";
    }

    localStorage.setItem("empData", JSON.stringify(employeeList));
    clearInputs();
    showEmployees();
}

function showEmployees() {
    tableBody.innerHTML = "";

    employeeList.forEach((emp, index) => {
        tableBody.innerHTML += `
            <tr>
                <td>${index + 1}</td>
                <td>${emp.id}</td>
                <td>${emp.name}</td>
                <td>${emp.dept}</td>
                <td>${emp.email}</td>
                <td>${emp.salary}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editEmployee(${index})">Edit</button>
                    <button class="action-btn delete-btn" onclick="deleteEmployee(${index})">Delete</button>
                </td>
            </tr>
        `;
    });

    empCount.innerText = employeeList.length;
}

function editEmployee(index) {
    const emp = employeeList[index];

    empId.value = emp.id;
    empName.value = emp.name;
    empDept.value = emp.dept;
    empEmail.value = emp.email;
    empSalary.value = emp.salary;

    editEmpIndex = index;
    btnSave.innerText = "Update Employee";
}

function deleteEmployee(index) {
    if (confirm("Delete this employee?")) {
        employeeList.splice(index, 1);
        localStorage.setItem("empData", JSON.stringify(employeeList));
        showEmployees();
    }
}

function clearInputs() {
    empId.value = "";
    empName.value = "";
    empDept.value = "";
    empEmail.value = "";
    empSalary.value = "";
}

showEmployees();