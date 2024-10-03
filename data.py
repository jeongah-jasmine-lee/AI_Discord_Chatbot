
# CS377 Topics (Retrieved from https://github.com/umass-cs-377/377-F22/blob/main/syllabus/syllabus.md)
topics = [
    "Processes and Process API",
    "System Calls",
    "Direct Execution",
    "CPU Scheduling",
    "Concurrency and Threads",
    "Locks and Event-based Concurrency",
    "Condition Variables, Semaphores, and Monitors",
    "I/O Devices, Disks, Files and Directories, and File System Implementation",
    "Address Spaces and the Memory API",
    "Address Translation and Segmentation",
    "Free Space Management and Paging",
    "Translation Lookaside Buffers and Page Tables"
]

# Multi-Choice Questions
multi_choice_qas = [
    {
        "question": "What is the primary function of an operating system?",
        "choices": ["A) Perform complex calculations", "B) Manage hardware and software resources", "C) Write and edit code", "D) Connect to the internet"],
        "correct": "B",
        "topic": "Processes and Process API",
        "explanation": "The operating system's primary role is to manage hardware resources and provide an environment where software can run efficiently."
    },
    {
        "question": "Which of the following is an example of volatile memory?",
        "choices": ["A) SSD (Solid State Drive)", "B) HDD (Hard Disk Drive)", "C) RAM (Random Access Memory)", "D) DVD"],
        "correct": "C",
        "topic": "Address Spaces and the Memory API",
        "explanation": "RAM is volatile memory, meaning its contents are lost when power is turned off, unlike SSDs, HDDs, or DVDs which are non-volatile."
    },
    {
        "question": "What does the acronym \"CPU\" stand for?",
        "choices": ["A) Central Processing Unit", "B) Central Power Unit", "C) Computer Processing Unit", "D) Control Processing Unit"],
        "correct": "A",
        "topic": "Direct Execution",
        "explanation": "The Central Processing Unit (CPU) is the core component that performs most of the data processing in a computer."
    },
    {
        "question": "Which of the following is NOT a type of system software?",
        "choices": ["A) Operating system", "B) Utility software", "C) Word processor", "D) Device drivers"],
        "correct": "C",
        "topic": "Processes and Process API",
        "explanation": "A word processor is application software, while operating systems, utility software, and device drivers are considered system software."
    },
    {
        "question": "In computing, what is 'virtual memory' used for?",
        "choices": ["A) Storing frequently used data for quick access", "B) Extending physical memory to the hard drive", "C) Compressing files", "D) Securing sensitive information"],
        "correct": "B",
        "topic": "Address Translation and Segmentation",
        "explanation": "Virtual memory allows the system to use hard drive space to extend the physical memory available for programs, enabling larger applications to run."
    },
    {
        "question": "Which of the following file systems is commonly used in Linux operating systems?",
        "choices": ["A) NTFS", "B) FAT32", "C) ext4", "D) HFS+"],
        "correct": "C",
        "topic": "Files and Directories",
        "explanation": "ext4 is the most widely used file system for Linux, providing stability and performance. NTFS is primarily used by Windows."
    },
    {
        "question": "What is the purpose of a device driver in a computer system?",
        "choices": ["A) It allows hardware to communicate with the operating system.", "B) It manages internet connections.", "C) It secures the system against malware.", "D) It increases the speed of the processor."],
        "correct": "A",
        "topic": "I/O Devices",
        "explanation": "Device drivers are software components that enable the operating system to interact with hardware devices such as printers, keyboards, or graphics cards."
    },
    {
        "question": "Which scheduling algorithm selects the job that arrives first for execution?",
        "choices": ["A) Round Robin", "B) Shortest Job First", "C) First-Come-First-Served", "D) Priority Scheduling"],
        "correct": "C",
        "topic": "CPU Scheduling",
        "explanation": "The First-Come-First-Served (FCFS) algorithm executes processes in the order they arrive in the queue, making it a simple scheduling method."
    },
    {
        "question": "What is the main function of the ALU (Arithmetic Logic Unit)?",
        "choices": ["A) Storing data permanently", "B) Processing input and output signals", "C) Performing arithmetic and logical operations", "D) Managing memory access"],
        "correct": "C",
        "topic": "Direct Execution",
        "explanation": "The ALU is responsible for performing mathematical and logical operations, such as addition, subtraction, and comparisons, within the CPU."
    },
    {
        "question": "Which type of memory is the fastest for the CPU to access?",
        "choices": ["A) Cache memory", "B) SSD", "C) RAM", "D) Hard disk"],
        "correct": "A",
        "topic": "Address Spaces and the Memory API",
        "explanation": "Cache memory is the fastest form of memory, located very close to the CPU, allowing quick access to frequently used data."
    },
]