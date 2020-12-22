#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "doc_struct.h"
#include "doc_processor.h"

int main()
{
    char test[] = "I.love.to dance.\nCoding.is my hobby.\nHey!.Beautiful girl.";
    printf("<Original text>\n%s\n", test);
    printf("len(test) = %zu\n", strlen(test));
    Doc* doc = get_document(test);
    doc_info(doc);
    release_doc(doc);
    return 0;
}
