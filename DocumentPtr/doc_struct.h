#ifndef DOCUMENT_STRUCTO_H
#define DOCUMENT_STRUCTO_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*------------------------------------------------
                TYPE DEFINITION
------------------------------------------------*/

typedef struct Sent{
    int data_num;
    char** words;
}Sent;

typedef struct Para{
    int data_num;
    Sent** sents;
}Para;

typedef struct Doc{
    int data_num;
    Para** paras;
}Doc;

/*------------------------------------------------
                FUNCTOIN DECLARATION
------------------------------------------------*/
Sent* _new_sent();
Para* _new_para();
Doc* _new_doc();

void sent_append(char* new_word, Sent* sent);
void para_append(Sent* new_sent, Para* para);
void doc_append(Para* new_para, Doc* doc);

void release_sent(Sent* sent);
void release_para(Para* para);
void release_doc(Doc* doc);

void sent_info(Sent* sent);
void para_info(Para* para);
void doc_info(Doc* doc);
#endif
