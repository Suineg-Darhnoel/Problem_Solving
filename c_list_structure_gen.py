import pathlib
c_list_struct_type = open("c_list_struct.h", "w")
c_list_struct_func = open("c_list_struct.c", "w")

CTYPES = {
            "INT":"int",
            "FLOAT":"float",
            "DOUBLE":"double",
            "CHAR":"char",
            "SHORT":"short",
            "LONG":"long"
        }

list_structure = """typedef struct List{0}{{
    int length;
    {1}* data;
}}List{0};
"""
list_functions = [
            # function to append
            "void list{0}_append({1} elem, List{0}*)",
            # function to print
            "void list{0}_print(List{0}* list, int verbose)",
            # function to release dynamically allocated memory
            "void list{0}_release(List{0}* list)",
            # init
            "List{0}* list{0}_new()"
        ]

list_func_templates = [
"""List{0}* list{0}_new()
{{
    List{0}* new_list = (List{0}*) malloc(sizeof(List{0}));
    new_list->length = 0;
    new_list->data = NULL;
    return new_list;
}}
""",
"""
void list{0}_append({1} elem, List{0}* list)
{{
    int len = ++list->length;
    list->data = ({1}*) realloc(list->data, sizeof({1})*len);
    if (list->data){{
        list->data[len-1] = elem;
    }}
    else{{
        exit(1);
    }}
}}
""",
#### FIX HERE ##################################
"""
void list{0}_print(List{0}* list, int verbose)
{{
    int i;
    if (verbose)
        printf("<Object <List{0}>at(%p)>\\n", list);
    printf("[ ");
    for (i = 0; i < list->length; i++){{
        printf("%{2} ", list->data[i]);
    }}
    puts("]");
}}
"""
"""
void list{0}_release(List{0}* list)
{{
    free(list->data);
    free(list);
}}
"""
]

if __name__ == "__main__":
    # write all types into c_list_type.h
    for ctype, base_type in CTYPES.items():
        # type structs
        list_struct_text = list_structure.format(ctype, base_type) + "\n"
        c_list_struct_type.write(list_struct_text)

    for ctype, base_type in CTYPES.items():
        # function declarations
        for lf in list_functions:
            func_declaration = lf + ";\n"
            list_func_text = func_declaration.format(ctype, base_type)
            print(list_func_text)
            c_list_struct_type.write(list_func_text)
        c_list_struct_type.write("\n")

    c_list_struct_func.write("#include <stdio.h>\n")
    c_list_struct_func.write("#include <stdlib.h>\n")
    c_list_struct_func.write("#include \"c_list_struct.h\"\n")

    ctype_format = {
                "char":"c",
                "int":"d",
                "short":"d",
                "long":"ld",
                "float":"f",
                "double":"lf"
            }

    for ctype, base_type in CTYPES.items():
        for lft in list_func_templates:
            functions_text = lft.format(ctype, base_type, ctype_format[base_type]);
            # print(lft.format(ctype, base_type))
            c_list_struct_func.write(functions_text)

    c_list_struct_type.close()
    c_list_struct_func.close()
