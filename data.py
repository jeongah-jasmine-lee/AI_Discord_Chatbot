
# CS377 Topics (Retrieved from https://github.com/umass-cs-377/377-F22/blob/main/syllabus/syllabus.md)
topics = {
    "1": "Processes and Process API",
    "2": "System Calls",
    "3": "Direct Execution",
    "4": "CPU Scheduling",
    "5": "Concurrency and Threads",
    "6": "Locks and Event-based Concurrency",
    "7": "Condition Variables, Semaphores, and Monitors",
    "8": "I/O Devices, Disks, Files and Directories, and File System Implementation",
    "9": "Address Spaces and the Memory API",
    "10": "Address Translation and Segmentation",
    "11": "Free Space Management and Paging",
    "12": "Translation Lookaside Buffers and Page Tables"
}

# Multi-Choice Questions
multi_choice_qas = [
    {
        "question": "What is the primary function of an operating system?",
        "choices": ["A) Perform complex calculations", "B) Manage hardware and software resources", "C) Write and edit code", "D) Connect to the internet"],
        "correct": "B",
        "topic": "1",
        "explanation": "The operating system's primary role is to manage hardware resources and provide an environment where software can run efficiently."
    },
    {
        "question": "What is a process in an operating system?",
        "choices": ["A) A passive entity like a file", "B) An instance of a running program", "C) A hardware component", "D) A data structure"],
        "correct": "B",
        "topic": "1",
        "explanation": "A process is an instance of a running program that includes the program code and its current activity."
    },
    {
        "question": "Which of the following is part of a process's machine state?",
        "choices": ["A) Program Counter", "B) Hard Disk", "C) CPU Fan", "D) Network Interface"],
        "correct": "A",
        "topic": "1",
        "explanation": "The machine state of a process includes components like the program counter, registers, and memory."
    },
    {
        "question": "What is the role of the Process Control Block (PCB)?",
        "choices": ["A) Manages system calls", "B) Tracks the current state of a process", "C) Schedules CPU resources", "D) Tracks hardware interrupts"],
        "correct": "B",
        "topic": "1",
        "explanation": "The Process Control Block stores information about a process's current state and resources."
    },
    {
        "question": "What system call creates a new process in UNIX-based systems?",
        "choices": ["A) exec()", "B) kill()", "C) fork()", "D) exit()"],
        "correct": "C",
        "topic": "1",
        "explanation": "The fork() system call is used in UNIX-based systems to create a new process by duplicating the current process."
    },
    {
        "question": "Which of the following is NOT a typical state of a process?",
        "choices": ["A) Running", "B) Ready", "C) Blocked", "D) Terminated"],
        "correct": "D",
        "topic": "1",
        "explanation": "A typical process moves between running, ready, and blocked states. A process that has completed is considered exited or finished."
    },
    {
        "question": "What happens during a context switch?",
        "choices": ["A) The process is terminated", "B) The OS switches between processes by saving and restoring states", "C) The CPU halts all processes", "D) Hardware is shut down temporarily"],
        "correct": "B",
        "topic": "1",
        "explanation": "During a context switch, the operating system saves the state of the current process and loads the state of the next process to execute."
    },
    {
        "question": "What is a zombie process?",
        "choices": ["A) A process waiting for CPU time", "B) A terminated process whose parent has not called wait()", "C) A process that never terminates", "D) A process in a blocked state"],
        "correct": "B",
        "topic": "1",
        "explanation": "A zombie process is one that has completed execution but still has an entry in the process table because the parent has not called wait()."
    },
    {
        "question": "What does the exec() system call do?",
        "choices": ["A) Create a new process", "B) Replace the current process image with a new one", "C) Terminate a process", "D) Put the process to sleep"],
        "correct": "B",
        "topic": "1",
        "explanation": "The exec() system call replaces the current process's memory image with a new program, effectively running a different program."
    },
    {
        "question": "Which of the following is true about process creation?",
        "choices": ["A) A process cannot create another process", "B) Processes can create other processes through system calls", "C) Processes can only be created by the kernel", "D) A process always terminates its parent upon creation"],
        "correct": "B",
        "topic": "1",
        "explanation": "Processes can create other processes through system calls like fork() in UNIX-based systems."
    },
    {
        "question": "What is the purpose of the wait() system call?",
        "choices": ["A) To wait for a specific I/O event", "B) To wait for the termination of a child process", "C) To put a process to sleep", "D) To create a process"],
        "correct": "B",
        "topic": "1",
        "explanation": "The wait() system call makes a parent process wait until its child process finishes execution."
    },
    {
        "question": "What is the typical result of a fork() system call?",
        "choices": ["A) No change in the process", "B) The creation of a new child process", "C) The termination of the current process", "D) Replacing the current process image"],
        "correct": "B",
        "topic": "1",
        "explanation": "The fork() system call results in the creation of a new child process that is an exact copy of the parent process."
    },
    {
        "question": "What does the term 'address space' refer to in a process?",
        "choices": ["A) The physical memory used by the OS", "B) The set of addresses that a process can use in its execution", "C) The disk space allocated to a process", "D) The address of the PCB"],
        "correct": "B",
        "topic": "1",
        "explanation": "The address space of a process refers to the set of memory addresses that it can access, which includes code, data, and stack segments."
    },
    {
        "question": "What does the system call kill() do?",
        "choices": ["A) Terminates the parent process", "B) Sends a signal to a process", "C) Deletes a file", "D) Blocks a process from running"],
        "correct": "B",
        "topic": "1",
        "explanation": "The kill() system call sends a signal to a process, which can be used to terminate it or perform other actions."
    },
    {
        "question": "What is the difference between a process and a thread?",
        "choices": ["A) A process has its own memory space, while threads share the same memory space", "B) A thread has its own memory space, while processes share the same memory space", "C) Threads cannot be scheduled by the OS", "D) Processes are faster than threads"],
        "correct": "A",
        "topic": "1",
        "explanation": "Processes have their own memory space, whereas threads share the same memory space within the same process."
    },
    {
        "question": "In UNIX, what system call does a process use to terminate itself?",
        "choices": ["A) kill()", "B) exit()", "C) exec()", "D) fork()"],
        "correct": "B",
        "topic": "1",
        "explanation": "The exit() system call is used by a process to terminate itself."
    },
    {
        "question": "Which data structure stores information about a process in an OS?",
        "choices": ["A) Process Control Block (PCB)", "B) File Descriptor Table", "C) Interrupt Vector Table", "D) System Call Table"],
        "correct": "A",
        "topic": "1",
        "explanation": "The Process Control Block (PCB) is a data structure that stores all information related to a process."
    },
    {
        "question": "Which of the following is an example of process creation in UNIX?",
        "choices": ["A) exec()", "B) fork()", "C) wait()", "D) exit()"],
        "correct": "B",
        "topic": "1",
        "explanation": "The fork() system call in UNIX creates a new child process."
    },
    {
        "question": "What is the purpose of the heap in a process's address space?",
        "choices": ["A) To store local variables", "B) To store dynamically allocated memory", "C) To store CPU instructions", "D) To store file descriptors"],
        "correct": "B",
        "topic": "1",
        "explanation": "The heap is used to store dynamically allocated memory during the process's execution."
    },
    {
        "question": "What happens when a process calls the exec() system call?",
        "choices": ["A) A new process is created", "B) The current process is replaced with a new program", "C) The process is terminated", "D) The process is paused"],
        "correct": "B",
        "topic": "1",
        "explanation": "The exec() system call replaces the current process image with a new program, continuing its execution."
    },
    {
        "question": "Which of the following is NOT a valid process state?",
        "choices": ["A) Running", "B) Waiting", "C) Sleeping", "D) Swapped"],
        "correct": "D",
        "topic": "1",
        "explanation": "In the typical process lifecycle, processes transition between states like running, ready, and waiting, but 'swapped' is not a common process state."
    },
    {
        "question": "Which of the following is NOT a type of system software?",
        "choices": ["A) Operating system", "B) Utility software", "C) Word processor", "D) Device drivers"],
        "correct": "C",
        "topic": "2",
        "explanation": "A word processor is application software, while operating systems, utility software, and device drivers are considered system software."
    },
    {
        "question": "What is a system call?",
        "choices": ["A) A request by a program to the OS for a service", "B) A call to a function in user space", "C) A hardware interrupt", "D) A request by the OS to the hardware"],
        "correct": "A",
        "topic": "2",
        "explanation": "A system call is a mechanism through which a program requests services from the operating system."
    },
    {
        "question": "Which system call is used to open a file in UNIX?",
        "choices": ["A) open()", "B) read()", "C) write()", "D) fork()"],
        "correct": "A",
        "topic": "2",
        "explanation": "The open() system call in UNIX is used to open a file and obtain a file descriptor."
    },
    {
        "question": "What happens when a process executes the exec() system call?",
        "choices": ["A) The process forks a child", "B) The current process is replaced by a new program", "C) The process continues to run without changes", "D) The process is terminated"],
        "correct": "B",
        "topic": "2",
        "explanation": "The exec() system call replaces the current process's memory with a new program."
    },
    {
        "question": "What is the function of the close() system call?",
        "choices": ["A) Closes a file descriptor", "B) Terminates a process", "C) Stops the execution of a program", "D) Closes an application"],
        "correct": "A",
        "topic": "2",
        "explanation": "The close() system call is used to close a file descriptor, freeing up resources."
    },
    {
        "question": "Which of the following system calls is used to read from a file?",
        "choices": ["A) write()", "B) open()", "C) read()", "D) exec()"],
        "correct": "C",
        "topic": "2",
        "explanation": "The read() system call is used to read data from a file descriptor."
    },
    {
        "question": "What does the kill() system call do?",
        "choices": ["A) Terminates a process", "B) Sends a signal to a process", "C) Stops the operating system", "D) Kills a thread"],
        "correct": "B",
        "topic": "2",
        "explanation": "The kill() system call sends a signal to a process, which can terminate the process or trigger another action."
    },
    {
        "question": "Which system call is used to change file permissions in UNIX?",
        "choices": ["A) chmod()", "B) chown()", "C) fork()", "D) exec()"],
        "correct": "A",
        "topic": "2",
        "explanation": "The chmod() system call is used to change the permissions of a file in UNIX-based systems."
    },
    {
        "question": "Which of the following system calls creates a new process?",
        "choices": ["A) exec()", "B) open()", "C) fork()", "D) read()"],
        "correct": "C",
        "topic": "2",
        "explanation": "The fork() system call creates a new process by duplicating the calling process."
    },
    {
        "question": "What does the wait() system call do?",
        "choices": ["A) Pauses a process", "B) Waits for a process to terminate", "C) Sends a signal to another process", "D) Halts the operating system"],
        "correct": "B",
        "topic": "2",
        "explanation": "The wait() system call makes the parent process wait until one of its child processes finishes execution."
    },
    {
        "question": "Which system call is used to write data to a file in UNIX?",
        "choices": ["A) read()", "B) open()", "C) write()", "D) fork()"],
        "correct": "C",
        "topic": "2",
        "explanation": "The write() system call is used to write data to a file descriptor."
    },
    {
        "question": "Which system call is used to replace the current process image with a new program?",
        "choices": ["A) exec()", "B) fork()", "C) exit()", "D) wait()"],
        "correct": "A",
        "topic": "2",
        "explanation": "The exec() system call replaces the current process image with a new program."
    },
    {
        "question": "Which system call is used to terminate the current process in UNIX?",
        "choices": ["A) exec()", "B) exit()", "C) kill()", "D) fork()"],
        "correct": "B",
        "topic": "2",
        "explanation": "The exit() system call terminates the current process and releases its resources."
    },
    {
        "question": "What does the chdir() system call do?",
        "choices": ["A) Changes the current working directory", "B) Changes the owner of a file", "C) Changes the permissions of a file", "D) Changes the process ID"],
        "correct": "A",
        "topic": "2",
        "explanation": "The chdir() system call changes the current working directory of a process."
    },
    {
        "question": "What does the pipe() system call do?",
        "choices": ["A) Duplicates a process", "B) Redirects input/output between processes", "C) Creates a thread", "D) Terminates a child process"],
        "correct": "B",
        "topic": "2",
        "explanation": "The pipe() system call is used to create a unidirectional communication channel between processes."
    },
    {
        "question": "Which system call is used to duplicate a file descriptor in UNIX?",
        "choices": ["A) fork()", "B) dup()", "C) exec()", "D) close()"],
        "correct": "B",
        "topic": "2",
        "explanation": "The dup() system call duplicates a file descriptor, making it refer to the same open file description."
    },
    {
        "question": "Which of the following is NOT a system call in UNIX?",
        "choices": ["A) open()", "B) write()", "C) close()", "D) printf()"],
        "correct": "D",
        "topic": "2",
        "explanation": "printf() is a library function in C, not a system call. System calls operate at the OS level."
    },
    {
        "question": "What is the purpose of the select() system call?",
        "choices": ["A) To monitor multiple file descriptors", "B) To send a signal to a process", "C) To create a new process", "D) To terminate a process"],
        "correct": "A",
        "topic": "2",
        "explanation": "The select() system call is used to monitor multiple file descriptors to see if they are ready for reading or writing."
    },
    {
        "question": "What is the role of the fstat() system call?",
        "choices": ["A) To terminate a process", "B) To retrieve information about a file", "C) To close a file", "D) To read from a file"],
        "correct": "B",
        "topic": "2",
        "explanation": "The fstat() system call retrieves information about a file, such as its size, permissions, and last modification time."
    },
    {
        "question": "Which system call is used to create a hard link in UNIX?",
        "choices": ["A) link()", "B) unlink()", "C) open()", "D) chown()"],
        "correct": "A",
        "topic": "2",
        "explanation": "The link() system call is used to create a hard link, which allows multiple directory entries to refer to the same file."
    },
    {
        "question": "Which system call in UNIX removes a directory entry?",
        "choices": ["A) unlink()", "B) open()", "C) read()", "D) exit()"],
        "correct": "A",
        "topic": "2",
        "explanation": "The unlink() system call removes a directory entry, effectively deleting the file."
    },
    {
        "question": "What does the acronym \"CPU\" stand for?",
        "choices": ["A) Central Processing Unit", "B) Central Power Unit", "C) Computer Processing Unit", "D) Control Processing Unit"],
        "correct": "A",
        "topic": "3",
        "explanation": "The Central Processing Unit (CPU) is the core component that performs most of the data processing in a computer."
    },
    {
        "question": "What is the main function of the ALU (Arithmetic Logic Unit)?",
        "choices": ["A) Storing data permanently", "B) Processing input and output signals", "C) Performing arithmetic and logical operations", "D) Managing memory access"],
        "correct": "C",
        "topic": "3",
        "explanation": "The ALU is responsible for performing mathematical and logical operations, such as addition, subtraction, and comparisons, within the CPU."
    },
    {
        "question": "What is the key goal of Direct Execution in an operating system?",
        "choices": ["A) To slow down program execution", "B) To prevent direct access to the CPU", "C) To make a program run as fast as possible", "D) To simplify process management"],
        "correct": "C",
        "topic": "3",
        "explanation": "Direct execution allows a program to run directly on the CPU, which improves performance by minimizing OS intervention."
    },
    {
        "question": "What is the main challenge of Direct Execution?",
        "choices": ["A) Inefficient CPU utilization", "B) Lack of hardware support", "C) Limited control over what a program can do", "D) Slower program execution"],
        "correct": "C",
        "topic": "3",
        "explanation": "The challenge is controlling what a program can do while ensuring it runs efficiently. Without control, a program could perform unauthorized actions."
    },
    {
        "question": "What is User Mode in the context of Direct Execution?",
        "choices": ["A) A restricted mode where a program can only execute non-privileged instructions", "B) A mode where a user interacts directly with hardware", "C) A privileged mode that allows full access to system resources", "D) A mode where the OS does not interact with the process"],
        "correct": "A",
        "topic": "3",
        "explanation": "In user mode, the program is restricted in what it can do, such as not being able to perform I/O operations or access hardware directly."
    },
    {
        "question": "What is Kernel Mode in Direct Execution?",
        "choices": ["A) A mode where the CPU is restricted", "B) A mode where the user process has full control", "C) A privileged mode that allows full access to system resources", "D) A debugging mode for user programs"],
        "correct": "C",
        "topic": "3",
        "explanation": "In kernel mode, the OS has full control over the CPU and system resources, allowing it to execute privileged operations such as handling I/O and memory management."
    },
    {
        "question": "What happens when a program running in user mode tries to perform an I/O operation?",
        "choices": ["A) The operation is performed directly", "B) The OS ignores the request", "C) The OS takes over via a system call", "D) The process is terminated"],
        "correct": "C",
        "topic": "3",
        "explanation": "If a program in user mode needs to perform an I/O operation, it issues a system call, allowing the OS to perform the operation on its behalf."
    },
    {
        "question": "Which instruction is used to switch from user mode to kernel mode?",
        "choices": ["A) fork()", "B) exec()", "C) trap", "D) kill()"],
        "correct": "C",
        "topic": "3",
        "explanation": "A trap instruction is used to switch from user mode to kernel mode. It allows the OS to handle system calls and other privileged operations."
    },
    {
        "question": "What does the OS do when a trap instruction is executed?",
        "choices": ["A) Terminates the current process", "B) Enters kernel mode to handle the system call", "C) Reboots the system", "D) Switches to another process"],
        "correct": "B",
        "topic": "3",
        "explanation": "When a trap instruction is executed, the OS switches to kernel mode to handle the system call or privileged operation requested by the user process."
    },
    {
        "question": "What is a context switch?",
        "choices": ["A) A process terminates and releases CPU resources", "B) The OS switches the CPU from one process to another", "C) The OS switches from kernel mode to user mode", "D) A process waits for I/O"],
        "correct": "B",
        "topic": "3",
        "explanation": "A context switch occurs when the OS saves the state of the current process and switches the CPU to another process, allowing multiple processes to share the CPU."
    },
    {
        "question": "What problem does context switching solve in Direct Execution?",
        "choices": ["A) Memory allocation", "B) CPU scheduling", "C) Virtual memory", "D) Time-sharing of CPU resources"],
        "correct": "D",
        "topic": "3",
        "explanation": "Context switching allows the OS to share CPU resources among multiple processes, which is essential for time-sharing systems."
    },
    {
        "question": "What is the purpose of a timer interrupt in Direct Execution?",
        "choices": ["A) To stop the process permanently", "B) To allow user processes to switch to kernel mode", "C) To prevent a single process from monopolizing the CPU", "D) To initiate a system call"],
        "correct": "C",
        "topic": "3",
        "explanation": "A timer interrupt ensures that the OS can regain control of the CPU and prevent any one process from monopolizing it."
    },
    {
        "question": "What happens when a user process performs an illegal operation?",
        "choices": ["A) The operation is ignored", "B) The process is terminated", "C) A trap is triggered and the OS handles the error", "D) The process switches to kernel mode"],
        "correct": "C",
        "topic": "3",
        "explanation": "When a user process performs an illegal operation, a trap is triggered, and the OS handles the exception, which could lead to process termination."
    },
    {
        "question": "What does the term 'privileged operation' mean in Direct Execution?",
        "choices": ["A) Operations that can only be performed by user programs", "B) Operations that require kernel mode access", "C) Operations that are executed faster than normal", "D) Operations that are restricted to specific users"],
        "correct": "B",
        "topic": "3",
        "explanation": "Privileged operations, such as managing memory or performing I/O, can only be performed in kernel mode to ensure system stability and security."
    },
    {
        "question": "What is the role of the OS during Direct Execution?",
        "choices": ["A) To execute all user instructions directly", "B) To control access to privileged instructions and resources", "C) To terminate user processes that are idle", "D) To handle only I/O operations"],
        "correct": "B",
        "topic": "3",
        "explanation": "During Direct Execution, the OS controls access to privileged instructions, system resources, and handles events like system calls and interrupts."
    },
    {
        "question": "How does the OS regain control from a user process during Direct Execution?",
        "choices": ["A) Through a system call or interrupt", "B) By forcibly terminating the process", "C) By waiting for the process to finish", "D) Through direct user input"],
        "correct": "A",
        "topic": "3",
        "explanation": "The OS regains control from a user process through system calls or interrupts, such as a timer interrupt or illegal operation."
    },
    {
        "question": "What is the role of the trap table in Direct Execution?",
        "choices": ["A) Stores user instructions", "B) Maps system calls to OS functions", "C) Schedules CPU resources", "D) Handles I/O operations"],
        "correct": "B",
        "topic": "3",
        "explanation": "The trap table maps system calls to their corresponding OS functions, allowing the OS to handle system calls made by user processes."
    },
    {
        "question": "What is the outcome of a return-from-trap instruction in Direct Execution?",
        "choices": ["A) The OS switches to kernel mode", "B) The process terminates", "C) The CPU returns to the user process and restores its previous state", "D) The OS switches to a different process"],
        "correct": "C",
        "topic": "3",
        "explanation": "A return-from-trap instruction restores the CPU state and returns control to the user process after the OS has handled the system call."
    },
    {
        "question": "Why is it important to distinguish between user mode and kernel mode?",
        "choices": ["A) To simplify process creation", "B) To prevent user programs from accessing privileged resources", "C) To allow direct memory access", "D) To improve CPU speed"],
        "correct": "B",
        "topic": "3",
        "explanation": "Distinguishing between user mode and kernel mode ensures that user programs cannot access privileged resources, such as memory management or I/O operations, directly."
    },
    {
        "question": "Which of the following is a key problem in Direct Execution?",
        "choices": ["A) Overuse of system calls", "B) Handling restricted operations and context switching", "C) Managing process creation", "D) Managing disk I/O"],
        "correct": "B",
        "topic": "3",
        "explanation": "Key problems in Direct Execution include managing restricted operations and efficiently switching contexts between processes."
    },
    {
        "question": "Which of the following actions requires a system call during Direct Execution?",
        "choices": ["A) Incrementing a variable", "B) Accessing hardware resources", "C) Multiplying two numbers", "D) Loading data into cache"],
        "correct": "B",
        "topic": "3",
        "explanation": "Accessing hardware resources, such as performing I/O operations, requires a system call, as user processes cannot directly interact with hardware."
    },
    {
        "question": "What is the function of the scheduler in Direct Execution?",
        "choices": ["A) To handle I/O operations", "B) To manage memory allocation", "C) To decide which process runs next", "D) To perform system calls"],
        "correct": "C",
        "topic": "3",
        "explanation": "The scheduler decides which process should run next, ensuring efficient CPU utilization and fair time-sharing between processes."
    },
    {
        "question": "Which scheduling algorithm selects the job that arrives first for execution?",
        "choices": ["A) Round Robin", "B) Shortest Job First", "C) First-Come-First-Served", "D) Priority Scheduling"],
        "correct": "C",
        "topic": "4",
        "explanation": "The First-Come-First-Served (FCFS) algorithm executes processes in the order they arrive in the queue, making it a simple scheduling method."
    },
    {
        "question": "What is the primary goal of CPU scheduling in an operating system?",
        "choices": ["A) Minimize memory usage", "B) Maximize CPU utilization", "C) Ensure process starvation", "D) Increase I/O wait time"],
        "correct": "B",
        "topic": "4",
        "explanation": "The primary goal of CPU scheduling is to maximize CPU utilization, ensuring that the CPU is busy as much as possible."
    },
    {
        "question": "What is turnaround time in CPU scheduling?",
        "choices": ["A) The time a process waits before it starts running", "B) The total time taken for a process from submission to completion", "C) The time taken for a context switch", "D) The time a process spends on I/O"],
        "correct": "B",
        "topic": "4",
        "explanation": "Turnaround time is the total time taken from the submission of a process to its completion, including waiting time and execution time."
    },
    {
        "question": "Which scheduling algorithm is also known as First-Come-First-Served (FCFS)?",
        "choices": ["A) Shortest Job First", "B) Round Robin", "C) First In, First Out", "D) Multilevel Feedback Queue"],
        "correct": "C",
        "topic": "4",
        "explanation": "First In, First Out (FIFO) is another name for First-Come-First-Served (FCFS) scheduling."
    },
    {
        "question": "Which scheduling algorithm is most appropriate for time-sharing systems?",
        "choices": ["A) Shortest Job First", "B) Round Robin", "C) First-Come-First-Served", "D) Priority Scheduling"],
        "correct": "B",
        "topic": "4",
        "explanation": "Round Robin is widely used in time-sharing systems because it allocates time slices to each process, ensuring no process is starved."
    },
    {
        "question": "In CPU scheduling, what is the convoy effect?",
        "choices": ["A) A process monopolizes the CPU", "B) I/O bound processes are stuck behind a CPU-bound process", "C) Processes arrive randomly", "D) CPU usage is maximized"],
        "correct": "B",
        "topic": "4",
        "explanation": "The convoy effect occurs when short I/O-bound processes get stuck behind long CPU-bound processes, leading to inefficient CPU utilization."
    },
    {
        "question": "What metric is improved by Shortest Job First (SJF) scheduling?",
        "choices": ["A) Response time", "B) Turnaround time", "C) Fairness", "D) Throughput"],
        "correct": "B",
        "topic": "4",
        "explanation": "Shortest Job First (SJF) minimizes the average turnaround time by scheduling shorter jobs first."
    },
    {
        "question": "What is the main disadvantage of the First-Come-First-Served (FCFS) scheduling algorithm?",
        "choices": ["A) High context-switch overhead", "B) Poor response time for long-running processes", "C) The convoy effect", "D) It is complex to implement"],
        "correct": "C",
        "topic": "4",
        "explanation": "The main disadvantage of FCFS is the convoy effect, where long processes can cause shorter processes to wait longer."
    },
    {
        "question": "What does the Round Robin scheduling algorithm aim to improve?",
        "choices": ["A) Turnaround time", "B) Response time", "C) Fairness", "D) I/O performance"],
        "correct": "B",
        "topic": "4",
        "explanation": "Round Robin aims to improve response time by ensuring each process gets a time slice at regular intervals."
    },
    {
        "question": "In which scheduling algorithm is a process moved between different priority queues based on its behavior?",
        "choices": ["A) First-Come-First-Served", "B) Shortest Job First", "C) Round Robin", "D) Multilevel Feedback Queue"],
        "correct": "D",
        "topic": "4",
        "explanation": "In Multilevel Feedback Queue scheduling, processes are moved between different priority queues depending on their CPU usage and behavior."
    },
    {
        "question": "What is the main problem with using the Shortest Job First (SJF) scheduling algorithm?",
        "choices": ["A) Requires knowledge of job length", "B) High overhead", "C) Poor turnaround time", "D) No fairness"],
        "correct": "A",
        "topic": "4",
        "explanation": "SJF requires knowing the length of each job in advance, which is difficult in most practical scenarios."
    },
    {
        "question": "In the context of CPU scheduling, what is response time?",
        "choices": ["A) The time from when a process is submitted until its first execution", "B) The time from submission to completion of a process", "C) The time spent waiting in the ready queue", "D) The time taken for a process to complete I/O"],
        "correct": "A",
        "topic": "4",
        "explanation": "Response time is the time from when a process is submitted until the first time it is scheduled to run."
    },
    {
        "question": "Which of the following is a preemptive CPU scheduling algorithm?",
        "choices": ["A) First-Come-First-Served", "B) Shortest Job First", "C) Round Robin", "D) Priority Scheduling without preemption"],
        "correct": "C",
        "topic": "4",
        "explanation": "Round Robin is a preemptive scheduling algorithm, meaning it preempts the running process after a fixed time slice."
    },
    {
        "question": "Which scheduling algorithm minimizes both turnaround time and response time in an ideal scenario?",
        "choices": ["A) First-Come-First-Served", "B) Round Robin", "C) Shortest Job First", "D) Multilevel Feedback Queue"],
        "correct": "C",
        "topic": "4",
        "explanation": "Shortest Job First (SJF) minimizes turnaround time and can achieve better response times when job lengths are known."
    },
    {
        "question": "What is the impact of a smaller time quantum in Round Robin scheduling?",
        "choices": ["A) Increases throughput", "B) Reduces context-switching overhead", "C) Improves response time but increases overhead", "D) Increases turnaround time"],
        "correct": "C",
        "topic": "4",
        "explanation": "Smaller time quanta improve response time but increase the overhead due to more frequent context switches."
    },
    {
        "question": "What is the key difference between Shortest Time-to-Completion First (STCF) and Shortest Job First (SJF)?",
        "choices": ["A) STCF is non-preemptive", "B) SJF is preemptive", "C) STCF is preemptive", "D) SJF minimizes response time"],
        "correct": "C",
        "topic": "4",
        "explanation": "Shortest Time-to-Completion First (STCF) is a preemptive version of SJF, allowing it to interrupt long jobs when shorter jobs arrive."
    },
    {
        "question": "What is starvation in the context of CPU scheduling?",
        "choices": ["A) A process that runs indefinitely", "B) A process that is blocked by I/O", "C) A low-priority process never getting CPU time", "D) A process that completes too quickly"],
        "correct": "C",
        "topic": "4",
        "explanation": "Starvation occurs when a low-priority process is perpetually prevented from getting CPU time due to the presence of higher-priority processes."
    },
    {
        "question": "What is the main advantage of Multilevel Feedback Queue (MLFQ) scheduling?",
        "choices": ["A) Simplicity", "B) Adaptability to process behavior", "C) Minimizing context switches", "D) Predictability"],
        "correct": "B",
        "topic": "4",
        "explanation": "MLFQ is highly adaptable because it changes process priorities based on their observed behavior, making it suitable for mixed workloads."
    },
    {
        "question": "In Round Robin scheduling, what happens if the time quantum is too large?",
        "choices": ["A) It behaves like First-Come-First-Served", "B) It increases context-switch overhead", "C) It improves response time", "D) It decreases CPU utilization"],
        "correct": "A",
        "topic": "4",
        "explanation": "If the time quantum is too large, Round Robin starts to behave like First-Come-First-Served (FCFS), as processes run to completion in their time slices."
    },
    {
        "question": "What does the term 'aging' refer to in CPU scheduling?",
        "choices": ["A) Increasing a process's priority over time to prevent starvation", "B) Decreasing a process's priority to improve fairness", "C) The CPU getting slower over time", "D) Prioritizing older processes"],
        "correct": "A",
        "topic": "4",
        "explanation": "Aging increases a process's priority the longer it waits in the system, helping to prevent starvation of low-priority processes."
    },
    {
        "question": "What is the main goal of preemptive scheduling algorithms like Shortest Time-to-Completion First (STCF)?",
        "choices": ["A) Minimize response time", "B) Ensure fairness", "C) Maximize I/O performance", "D) Minimize context switches"],
        "correct": "A",
        "topic": "4",
        "explanation": "Preemptive scheduling algorithms like STCF aim to minimize response time by preempting longer jobs in favor of shorter ones."
    },
    {
        "question": "What is the main reason for using threads in a program?",
        "choices": ["A) To reduce memory usage", "B) To achieve parallelism and avoid blocking due to I/O", "C) To simplify process scheduling", "D) To minimize the need for system calls"],
        "correct": "B",
        "topic": "5",
        "explanation": "Threads are used to achieve parallelism by performing multiple tasks simultaneously and avoid blocking when a thread waits for I/O."
    },
    {
        "question": "In a multi-threaded program, what do threads typically share?",
        "choices": ["A) Registers", "B) Program counter", "C) Address space", "D) Thread control block"],
        "correct": "C",
        "topic": "5",
        "explanation": "Threads within the same process share the same address space, which makes it easier to share data between threads."
    },
    {
        "question": "What is a key disadvantage of using processes instead of threads?",
        "choices": ["A) Processes cannot be preempted", "B) Processes have no shared memory", "C) Processes have higher overhead due to separate address spaces", "D) Processes cannot communicate with each other"],
        "correct": "C",
        "topic": "5",
        "explanation": "Processes have separate address spaces, which creates more overhead in memory management and makes sharing data more complex compared to threads."
    },
    {
        "question": "Which of the following statements is true about concurrency?",
        "choices": ["A) Concurrency only occurs in distributed systems", "B) Concurrency allows multiple tasks to make progress without waiting", "C) Concurrency guarantees that all tasks run simultaneously", "D) Concurrency requires multiple CPUs"],
        "correct": "B",
        "topic": "5",
        "explanation": "Concurrency allows multiple tasks to progress independently, often by interleaving their execution or using time-slicing, even on a single CPU."
    },
    {
        "question": "What does the term 'thread-local storage' refer to?",
        "choices": ["A) Shared memory between threads", "B) Memory that is unique to each thread", "C) The stack of the process", "D) A global variable shared by all threads"],
        "correct": "B",
        "topic": "5",
        "explanation": "Thread-local storage refers to memory that is unique to each thread and not shared with other threads in the same process."
    },
    {
        "question": "What happens when a thread performs a blocking I/O operation?",
        "choices": ["A) The thread is terminated", "B) The entire process is blocked", "C) Only the thread is blocked, and the CPU can execute other threads", "D) The thread waits for the next time slice"],
        "correct": "C",
        "topic": "5",
        "explanation": "When a thread performs a blocking I/O operation, only that thread is blocked while other threads can continue to run."
    },
    {
        "question": "What problem does uncontrolled scheduling cause in multithreaded programs?",
        "choices": ["A) Deadlocks", "B) Starvation", "C) Race conditions", "D) High CPU utilization"],
        "correct": "C",
        "topic": "5",
        "explanation": "Uncontrolled scheduling in multithreaded programs can lead to race conditions where the outcome depends on the order of execution of threads."
    },
    {
        "question": "What is the main difference between a process and a thread?",
        "choices": ["A) Threads run faster than processes", "B) Threads share the same memory space, while processes do not", "C) Threads require more resources than processes", "D) Processes can run in parallel, while threads cannot"],
        "correct": "B",
        "topic": "5",
        "explanation": "Threads within the same process share the same memory space, which makes communication between threads easier compared to separate processes."
    },
    {
        "question": "Why do modern operating systems use threads for many server-based applications?",
        "choices": ["A) Threads are easier to debug", "B) Threads allow overlap of computation and I/O", "C) Threads minimize the use of memory", "D) Threads prevent race conditions"],
        "correct": "B",
        "topic": "5",
        "explanation": "Threads are used in server-based applications to overlap computation and I/O, allowing more efficient use of resources like CPU and memory."
    },
    {
        "question": "What is a race condition?",
        "choices": ["A) When two threads modify shared data without proper synchronization", "B) When two processes compete for CPU resources", "C) When a process cannot access a resource due to deadlock", "D) When a process waits indefinitely for a resource"],
        "correct": "A",
        "topic": "5",
        "explanation": "A race condition occurs when two threads concurrently modify shared data without proper synchronization, leading to unpredictable outcomes."
    },
    {
        "question": "What is the purpose of the thread control block (TCB)?",
        "choices": ["A) To manage thread creation", "B) To store the thread's state and information", "C) To store process information", "D) To manage thread-local storage"],
        "correct": "B",
        "topic": "5",
        "explanation": "The thread control block (TCB) stores the thread's state and other information necessary for the OS to manage and schedule threads."
    },
    {
        "question": "How do threads in a multithreaded program improve CPU utilization?",
        "choices": ["A) By sharing the same CPU core", "B) By overlapping computation and I/O", "C) By running all threads on separate cores", "D) By reducing context-switch time"],
        "correct": "B",
        "topic": "5",
        "explanation": "Threads can improve CPU utilization by allowing one thread to run while another thread waits for I/O, maximizing the CPU’s use."
    },
    {
        "question": "Which of the following describes the difference between single-threaded and multi-threaded processes?",
        "choices": ["A) Single-threaded processes use multiple CPUs, while multi-threaded processes use one", "B) Single-threaded processes have one thread of control, while multi-threaded processes have multiple threads", "C) Multi-threaded processes have more memory overhead than single-threaded ones", "D) Single-threaded processes are always faster than multi-threaded processes"],
        "correct": "B",
        "topic": "5",
        "explanation": "Single-threaded processes have only one thread of control, while multi-threaded processes can run multiple threads simultaneously within the same process."
    },
    {
        "question": "Which of the following is a common issue that arises when using threads in concurrent programs?",
        "choices": ["A) High memory usage", "B) Deadlock", "C) Decreased CPU performance", "D) No process isolation"],
        "correct": "B",
        "topic": "5",
        "explanation": "A common issue when using threads is deadlock, which occurs when threads are waiting on each other indefinitely for resources."
    },
    {
        "question": "What is a thread's program counter responsible for?",
        "choices": ["A) Managing the thread's local memory", "B) Keeping track of the next instruction to execute", "C) Managing shared memory", "D) Keeping track of the process's global state"],
        "correct": "B",
        "topic": "5",
        "explanation": "The program counter of a thread keeps track of the next instruction the thread will execute."
    },
    {
        "question": "What does the term 'parallelism' refer to in the context of threads?",
        "choices": ["A) Running multiple threads in quick succession", "B) Running multiple threads simultaneously on multiple processors", "C) Creating multiple threads for a single task", "D) Running multiple tasks sequentially on a single CPU"],
        "correct": "B",
        "topic": "5",
        "explanation": "Parallelism refers to running multiple threads at the same time on multiple processors, which can significantly speed up execution."
    },
    {
        "question": "What is the primary advantage of using threads over processes?",
        "choices": ["A) Threads consume fewer CPU cycles", "B) Threads can access each other's memory", "C) Threads are easier to debug", "D) Threads have more security than processes"],
        "correct": "B",
        "topic": "5",
        "explanation": "Threads within the same process share memory, making inter-thread communication faster and more efficient than communication between processes."
    },
    {
        "question": "What is the role of the OS scheduler in a multithreaded environment?",
        "choices": ["A) To manage memory allocation for threads", "B) To schedule CPU time for each thread", "C) To manage file access for threads", "D) To create and terminate threads"],
        "correct": "B",
        "topic": "5",
        "explanation": "The OS scheduler assigns CPU time to each thread, ensuring that each thread gets a fair share of the CPU."
    },
    {
        "question": "In a system with concurrency, which of the following is necessary for proper synchronization between threads?",
        "choices": ["A) Shared memory", "B) Locks or other synchronization mechanisms", "C) A single CPU core", "D) No I/O operations"],
        "correct": "B",
        "topic": "5",
        "explanation": "Synchronization mechanisms like locks are essential in a multithreaded environment to ensure that multiple threads do not access shared resources concurrently and cause race conditions."
    },
    {
        "question": "What can result from two or more threads trying to modify a shared variable simultaneously without synchronization?",
        "choices": ["A) Starvation", "B) A race condition", "C) Deadlock", "D) Context switching"],
        "correct": "B",
        "topic": "5",
        "explanation": "A race condition occurs when two or more threads modify a shared variable at the same time without synchronization, leading to unpredictable results."
    },
    {
        "question": "What is the primary purpose of a lock in concurrent programming?",
        "choices": ["A) To speed up program execution", "B) To prevent multiple threads from accessing shared resources simultaneously", "C) To allow simultaneous I/O operations", "D) To prevent context switching"],
        "correct": "B",
        "topic": "6",
        "explanation": "Locks are used to prevent multiple threads from accessing shared resources concurrently, ensuring data consistency and preventing race conditions."
    },
    {
        "question": "Which of the following best defines a critical section?",
        "choices": ["A) A part of the program that performs I/O operations", "B) A section of code that accesses shared resources", "C) A part of the program that handles context switching", "D) A block of code that initializes a thread"],
        "correct": "B",
        "topic": "6",
        "explanation": "A critical section is a block of code that accesses shared resources and must not be executed by more than one thread at a time."
    },
    {
        "question": "Which of the following problems can occur if a thread fails to release a lock after entering a critical section?",
        "choices": ["A) Starvation", "B) Deadlock", "C) Race condition", "D) Context switching"],
        "correct": "B",
        "topic": "6",
        "explanation": "If a thread fails to release a lock, it can lead to deadlock, where other threads cannot proceed because they are waiting for the lock to be released."
    },
    {
        "question": "What is the main disadvantage of using spinlocks?",
        "choices": ["A) They increase memory usage", "B) They cause busy waiting, wasting CPU cycles", "C) They prevent context switching", "D) They increase the likelihood of race conditions"],
        "correct": "B",
        "topic": "6",
        "explanation": "Spinlocks cause busy waiting, where a thread continuously checks for a lock to be released, wasting CPU cycles if the lock is held for a long time."
    },
    {
        "question": "What is a deadlock in the context of concurrency?",
        "choices": ["A) When two threads modify the same variable simultaneously", "B) When threads hold locks and wait indefinitely for each other", "C) When a thread is never scheduled to run", "D) When a process waits for an I/O operation to complete"],
        "correct": "B",
        "topic": "6",
        "explanation": "A deadlock occurs when two or more threads hold locks and wait indefinitely for each other to release them, causing the program to halt."
    },
    {
        "question": "Which of the following is NOT a common strategy for preventing deadlocks?",
        "choices": ["A) Lock ordering", "B) Circular wait prevention", "C) Preemption", "D) Increasing thread priority"],
        "correct": "D",
        "topic": "6",
        "explanation": "Preventing deadlocks typically involves lock ordering, circular wait prevention, or preemption, but increasing thread priority does not prevent deadlocks."
    },
    {
        "question": "What is a condition variable used for in event-based concurrency?",
        "choices": ["A) To implement busy waiting", "B) To signal between threads when certain conditions are met", "C) To block threads indefinitely", "D) To prioritize CPU usage"],
        "correct": "B",
        "topic": "6",
        "explanation": "A condition variable is used to signal between threads when certain conditions are met, enabling one thread to wait for an event triggered by another."
    },
    {
        "question": "What is the difference between a mutex and a spinlock?",
        "choices": ["A) A mutex causes a context switch when waiting, while a spinlock uses busy waiting", "B) A spinlock can be held by multiple threads, while a mutex cannot", "C) A mutex is faster than a spinlock", "D) A spinlock is used in user space, while a mutex is used in kernel space"],
        "correct": "A",
        "topic": "6",
        "explanation": "A mutex causes a context switch when waiting for the lock, while a spinlock uses busy waiting, continuously checking if the lock is available."
    },
    {
        "question": "What is the primary benefit of using a condition variable in concurrency?",
        "choices": ["A) It reduces memory usage", "B) It prevents race conditions", "C) It allows threads to wait efficiently for a condition to be met", "D) It speeds up thread execution"],
        "correct": "C",
        "topic": "6",
        "explanation": "A condition variable allows threads to wait efficiently for a condition to be met, without busy waiting, thus saving CPU resources."
    },
    {
        "question": "What is the key problem that synchronization mechanisms like locks are designed to solve?",
        "choices": ["A) Deadlocks", "B) Race conditions", "C) Starvation", "D) CPU underutilization"],
        "correct": "B",
        "topic": "6",
        "explanation": "Locks and other synchronization mechanisms are primarily designed to prevent race conditions by ensuring that only one thread can access a critical section at a time."
    },
    {
        "question": "What is the term used to describe when two threads hold resources the other needs, leading to a deadlock?",
        "choices": ["A) Circular wait", "B) Starvation", "C) Livelock", "D) Preemption"],
        "correct": "A",
        "topic": "6",
        "explanation": "Circular wait is a condition where two or more threads hold resources the others need, leading to a deadlock."
    },
    {
        "question": "Which of the following is an example of busy waiting?",
        "choices": ["A) Using a condition variable to wait for an event", "B) Continuously checking if a lock is available", "C) Waiting for a thread to complete", "D) Using a semaphore to control access to resources"],
        "correct": "B",
        "topic": "6",
        "explanation": "Busy waiting occurs when a thread continuously checks if a lock is available, consuming CPU resources without making progress."
    },
    {
        "question": "How does the OS detect deadlocks?",
        "choices": ["A) By checking the process control block", "B) By monitoring thread priority", "C) By using a resource allocation graph", "D) By using condition variables"],
        "correct": "C",
        "topic": "6",
        "explanation": "The OS can detect deadlocks using a resource allocation graph, which helps identify circular wait conditions that indicate a deadlock."
    },
    {
        "question": "Which mechanism allows one thread to wait for another thread to signal that it has completed a task?",
        "choices": ["A) Locks", "B) Condition variables", "C) Semaphores", "D) Spinlocks"],
        "correct": "B",
        "topic": "6",
        "explanation": "Condition variables allow one thread to wait until another thread signals that a condition has been met, making them useful for coordinating tasks."
    },
    {
        "question": "What is a semaphore in the context of concurrency?",
        "choices": ["A) A lock that allows multiple threads to access a resource simultaneously", "B) A signaling mechanism to control access to resources", "C) A variable that stores the state of a thread", "D) A mechanism to speed up thread execution"],
        "correct": "B",
        "topic": "6",
        "explanation": "A semaphore is a signaling mechanism used to control access to resources, allowing threads to signal each other about the availability of resources."
    },
    {
        "question": "Which of the following is true about the priority inversion problem?",
        "choices": ["A) A lower-priority thread holds a resource needed by a higher-priority thread", "B) A higher-priority thread always runs before a lower-priority thread", "C) Two threads switch priorities", "D) A thread with the highest priority gets blocked indefinitely"],
        "correct": "A",
        "topic": "6",
        "explanation": "Priority inversion occurs when a lower-priority thread holds a resource that a higher-priority thread needs, causing the higher-priority thread to wait."
    },
    {
        "question": "What does the term 'livelock' refer to in concurrency?",
        "choices": ["A) Threads are waiting indefinitely for each other", "B) Threads are making progress but not completing their tasks", "C) A deadlock where two threads are stuck in a loop", "D) A state where the CPU is underutilized"],
        "correct": "B",
        "topic": "6",
        "explanation": "Livelock occurs when threads are not blocked but continue to change state without making any real progress, usually due to constant interaction."
    },
    {
        "question": "What is the primary purpose of using locks and condition variables together?",
        "choices": ["A) To reduce CPU usage", "B) To ensure that a thread can wait for a condition and avoid busy waiting", "C) To minimize memory overhead", "D) To reduce context switches"],
        "correct": "B",
        "topic": "6",
        "explanation": "Locks and condition variables are often used together to ensure that a thread can wait for a condition without busy waiting, allowing other threads to proceed."
    },
    {
        "question": "Which of the following is a key difference between a lock and a semaphore?",
        "choices": ["A) A semaphore can allow multiple threads to access a resource, while a lock cannot", "B) A lock is faster than a semaphore", "C) A lock allows context switching", "D) A semaphore always leads to deadlocks"],
        "correct": "A",
        "topic": "6",
        "explanation": "A key difference is that a semaphore can allow multiple threads to access a resource at the same time, while a lock only allows one thread."
    },
    {
        "question": "What is the main role of a condition variable in event-based concurrency?",
        "choices": ["A) To allow multiple threads to acquire a lock", "B) To signal that a particular event has occurred", "C) To block a thread indefinitely", "D) To reduce memory usage"],
        "correct": "B",
        "topic": "6",
        "explanation": "A condition variable is used to signal between threads that a specific event has occurred, allowing for synchronization between them."
    },
    {
        "question": "Which of the following file systems is commonly used in Linux operating systems?",
        "choices": ["A) NTFS", "B) FAT32", "C) ext4", "D) HFS+"],
        "correct": "C",
        "topic": "8",
        "explanation": "ext4 is the most widely used file system for Linux, providing stability and performance. NTFS is primarily used by Windows."
    },
    {
        "question": "What is the purpose of a device driver in a computer system?",
        "choices": ["A) It allows hardware to communicate with the operating system.", "B) It manages internet connections.", "C) It secures the system against malware.", "D) It increases the speed of the processor."],
        "correct": "A",
        "topic": "8",
        "explanation": "Device drivers are software components that enable the operating system to interact with hardware devices such as printers, keyboards, or graphics cards."
    },
    {
        "question": "What is the purpose of a device driver in an operating system?",
        "choices": ["A) To convert user requests into machine code", "B) To allow the OS to interact with hardware devices", "C) To manage file system operations", "D) To schedule CPU tasks"],
        "correct": "B",
        "topic": "8",
        "explanation": "A device driver is a software component that allows the operating system to communicate with hardware devices, such as printers and disks."
    },
    {
        "question": "Which of the following is NOT an I/O device classification?",
        "choices": ["A) Block devices", "B) Character devices", "C) Network devices", "D) Sequential devices"],
        "correct": "D",
        "topic": "8",
        "explanation": "I/O devices are generally classified as block devices, character devices, or network devices. Sequential devices are not a common classification."
    },
    {
        "question": "What is the key function of a file system in an OS?",
        "choices": ["A) To manage CPU processes", "B) To manage the organization and retrieval of data on a disk", "C) To manage memory allocation", "D) To handle I/O interrupts"],
        "correct": "B",
        "topic": "8",
        "explanation": "A file system is responsible for organizing and managing the storage and retrieval of data on disk, providing abstractions like files and directories."
    },
    {
        "question": "What does the term 'block device' refer to in I/O systems?",
        "choices": ["A) A device that can only perform sequential access", "B) A device that allows reading and writing fixed-size blocks of data", "C) A device that handles keyboard input", "D) A device that stores data in memory"],
        "correct": "B",
        "topic": "8",
        "explanation": "A block device is a hardware device that allows reading and writing in fixed-size blocks, such as disk drives."
    },
    {
        "question": "Which of the following is an example of a file system abstraction?",
        "choices": ["A) CPU", "B) RAM", "C) File", "D) Process"],
        "correct": "C",
        "topic": "8",
        "explanation": "A file is a key abstraction provided by a file system, representing a linear array of bytes stored on persistent storage."
    },
    {
        "question": "What is a directory in a file system?",
        "choices": ["A) A file that contains data", "B) A structure that stores metadata of files", "C) A special file that contains a list of files and subdirectories", "D) A memory management unit"],
        "correct": "C",
        "topic": "8",
        "explanation": "A directory is a special type of file that contains a list of files and subdirectories, allowing for the organization of files in a hierarchical structure."
    },
    {
        "question": "What is the main advantage of Direct Memory Access (DMA) in I/O operations?",
        "choices": ["A) It allows faster CPU scheduling", "B) It enables the CPU to perform I/O operations without blocking", "C) It reduces CPU overhead by allowing the transfer of data directly between memory and devices", "D) It reduces the time to access data in memory"],
        "correct": "C",
        "topic": "8",
        "explanation": "DMA allows the CPU to offload data transfer tasks to specialized hardware, reducing CPU overhead by directly transferring data between memory and devices."
    },
    {
        "question": "Which of the following is an example of a file metadata attribute?",
        "choices": ["A) File contents", "B) File name", "C) File extension", "D) File access permissions"],
        "correct": "D",
        "topic": "8",
        "explanation": "File access permissions are an example of metadata stored by the file system, which controls who can read, write, or execute a file."
    },
    {
        "question": "What does the term 'seek time' refer to in the context of disk I/O?",
        "choices": ["A) The time taken to read data from disk", "B) The time taken to move the disk arm to the correct track", "C) The time taken to transfer data from disk to memory", "D) The time taken to rotate the disk to the correct sector"],
        "correct": "B",
        "topic": "8",
        "explanation": "Seek time refers to the time it takes for the disk arm to move to the correct track before reading or writing data."
    },
    {
        "question": "Which disk scheduling algorithm is prone to starvation?",
        "choices": ["A) First-Come, First-Served (FCFS)", "B) Shortest Seek Time First (SSTF)", "C) SCAN", "D) C-SCAN"],
        "correct": "B",
        "topic": "8",
        "explanation": "SSTF prioritizes the request closest to the disk head, which can lead to starvation if requests for distant sectors are constantly delayed."
    },
    {
        "question": "What is a file descriptor?",
        "choices": ["A) A pointer to a file", "B) A data structure that stores file contents", "C) An integer used by the OS to access files", "D) A memory address"],
        "correct": "C",
        "topic": "8",
        "explanation": "A file descriptor is an integer that the operating system uses to uniquely identify an open file and allow processes to perform I/O operations."
    },
    {
        "question": "Which file system operation is atomic with respect to system crashes?",
        "choices": ["A) Reading a file", "B) Writing to a file", "C) Renaming a file", "D) Deleting a file"],
        "correct": "C",
        "topic": "8",
        "explanation": "Renaming a file is typically implemented as an atomic operation, ensuring that the file will either retain its old name or be fully renamed, with no intermediate state."
    },
    {
        "question": "What is the primary difference between SSD and HDD?",
        "choices": ["A) SSDs are more prone to failure", "B) SSDs use spinning platters", "C) SSDs are faster but more expensive than HDDs", "D) SSDs have a higher seek time"],
        "correct": "C",
        "topic": "8",
        "explanation": "SSDs are faster than HDDs because they use flash memory rather than spinning platters, but they are generally more expensive."
    },
    {
        "question": "What is the role of the superblock in a file system?",
        "choices": ["A) It stores file contents", "B) It stores the file system's metadata, such as the number of inodes and blocks", "C) It stores user data", "D) It stores the bootloader"],
        "correct": "B",
        "topic": "8",
        "explanation": "The superblock contains the file system's metadata, including information about the total number of inodes, blocks, and other critical data."
    },
    {
        "question": "What does the SCAN disk scheduling algorithm do?",
        "choices": ["A) It services requests in a circular manner", "B) It services the closest I/O request first", "C) It scans the disk back and forth, servicing requests in one direction per pass", "D) It services requests based on the process priority"],
        "correct": "C",
        "topic": "8",
        "explanation": "The SCAN algorithm, also known as the elevator algorithm, moves back and forth across the disk, servicing requests in one direction before changing direction."
    },
    {
        "question": "What is rotational latency in a hard disk?",
        "choices": ["A) The time taken to transfer data", "B) The time taken to move the disk arm", "C) The time taken for the desired sector to rotate under the disk head", "D) The time taken to execute a write command"],
        "correct": "C",
        "topic": "8",
        "explanation": "Rotational latency is the time it takes for the desired sector to rotate under the disk head, after the disk arm has been positioned on the correct track."
    },
    {
        "question": "What is the purpose of the inode in a file system?",
        "choices": ["A) To store the file's data", "B) To store the file's metadata", "C) To store the file's path", "D) To manage memory allocation for files"],
        "correct": "B",
        "topic": "8",
        "explanation": "The inode stores metadata about the file, such as its size, ownership, access permissions, and pointers to the data blocks on disk."
    },
    {
        "question": "What happens when you delete a file in most file systems?",
        "choices": ["A) The file data is immediately removed", "B) The file is removed from the directory but the data remains on disk until overwritten", "C) The file is moved to a backup partition", "D) The file's data is securely erased"],
        "correct": "B",
        "topic": "8",
        "explanation": "When a file is deleted, its entry is removed from the directory, but the actual data remains on the disk until it is overwritten by new data."
    },
    {
        "question": "What is a hard link in a file system?",
        "choices": ["A) A pointer to a symbolic link", "B) A duplicate copy of a file", "C) A direct pointer to the same inode as another file", "D) A file that contains a reference to another file's location"],
        "correct": "C",
        "topic": "8",
        "explanation": "A hard link creates a direct reference to the same inode, meaning both the original file and the hard link point to the same file data on disk."
    },
    {
        "question": "Why is disk scheduling important in operating systems?",
        "choices": ["A) To improve the speed of CPU operations", "B) To ensure fairness in resource allocation", "C) To reduce seek time and improve I/O performance", "D) To prevent deadlocks in I/O operations"],
        "correct": "C",
        "topic": "8",
        "explanation": "Disk scheduling is important because it reduces seek time by determining the order of I/O operations, improving overall I/O performance."
    },
    {
        "question": "Which type of memory is the fastest for the CPU to access?",
        "choices": ["A) Cache memory", "B) SSD", "C) RAM", "D) Hard disk"],
        "correct": "A",
        "topic": "9",
        "explanation": "Cache memory is the fastest form of memory, located very close to the CPU, allowing quick access to frequently used data."
    },
    {
        "question": "Which of the following is an example of volatile memory?",
        "choices": ["A) SSD (Solid State Drive)", "B) HDD (Hard Disk Drive)", "C) RAM (Random Access Memory)", "D) DVD"],
        "correct": "C",
        "topic": "9",
        "explanation": "RAM is volatile memory, meaning its contents are lost when power is turned off, unlike SSDs, HDDs, or DVDs which are non-volatile."
    },
    {
        "question": "In computing, what is 'virtual memory' used for?",
        "choices": ["A) Storing frequently used data for quick access", "B) Extending physical memory to the hard drive", "C) Compressing files", "D) Securing sensitive information"],
        "correct": "B",
        "topic": "10",
        "explanation": "Virtual memory allows the system to use hard drive space to extend the physical memory available for programs, enabling larger applications to run."
    },
]