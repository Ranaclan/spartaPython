# Linux Research

* [File ownership](#file-ownership)
* [File permissions](#file-permissions)
* [Numeric values](#numeric-values)
* [Changing file permissions](#changing-file-permissions)

## File ownership

### Why is managing file ownership important?
Files may contain sensitive information that only authorised users should be able to access

### What is the command to view file ownership?
```bash
ls -l
```

Returns a list of files as well as detailed information such as their owner and permission settings 

### What permissions are set when a user creates a file or directory? Who does file or directory belong to?
The file belongs to the user who created it. This user has read and writes permissions. Users who are part of the same group have read permissions. Other users have no permissions.

### Why does the owner, by default, not receive X permissions when they create a file?
Files are often not intended to be executed, or may result in a security vulnerability if executed.

### What command is used to change the owner of a file or directory?
```bash
chown [options] user[:group] file(s)
```

* options: Optional options
* user: The user who will become the new owner of the specified file(s)
* group: Optional group which will gain owner permissions
* file(s): The file(s) whose ownership will change

## File permissions

### Does being the owner of a file mean you have full permissions on that file? Explain.
Not necessarily. The file owner has a certain set of permissions, in the same way the group and other users have a set of permissions.

### If you give permissions to the User entity, what does this mean?
The owner of a specified file will now have the specified permissions to that file.

### If you give permissions to the Group entity, what does this mean?
All users within the specified group will now have the specified permissions to the specified file.

### If you give permissions to the Other entity, what does this mean?
All users will now have the specified permissions to the specified file.

### You give the following permissions to a file: User permissions are read-only, Group permissions are read and write, Other permissions are read, write and execute. You are logged in as the user which is owner of the file. What permissions will you have on this file? Explain.
I will have read-only permissions, as I am the owner and the owner (user) permissions on the file are set to read-only.

### Here is one line from the ls -l. Work everything you can about permissions on this file or directory.
```bash
-rwxr-xr-- 1 tcboony staff  123 Nov 25 18:36 keeprunning.sh
```

Owner permissions | Group Permissions | Other permissions
-|-|-|
Read, write and execute | Read and execute | Read only

## Numeric values

### What numeric values are assigned to each permission?
Read | Write | Execute
-|-|-
4|2|1

### What can you with the values assign read + write permissions?
4 + 2 = 6

### What value would assign read, write and execute permissions?
4 + 2 + 1 = 7

### What value would assign read and execute permissions?
2 + 1 = 3

### Often, a file or directory's mode/permissions are represented by 3 numbers. What do you think 644 would mean?
Owner permissions | Group Permissions | Other permissions
-|-|-
Read and write | Read only         | Read only

## Changing file permissions

### What command changes file permissions?
```bash
chmod [options] mode file
```

* options: Optional options
* mode: The new permissions, represented by 3 numbers
* file: The file whose permissions will change

### To change permissions on a file what must the end user be? (2 answers)
Either the owner of the file or the root user

### Give examples of some different ways/syntaxes to set permissions on a new file (named testfile.txt) to:
Set User to read, Group to read + write + execute, and Other to read and write only
```bash
chmod 476 testfile.txt
```

Add execute permissions (to all entities)
```bash
chmod +x testfile.txt
```

Take write permissions away from Group
```bash
chmod g-w testfile.txt
```

Use numeric values to give read + write access to User, read access to Group, and no access to Other.
```bash
chmod 640 testfile.txt
```