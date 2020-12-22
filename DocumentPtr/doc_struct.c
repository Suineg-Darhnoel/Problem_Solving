#include "doc_struct.h"

/*-------------------------------------------------
                    INIT FUNCTIONS
-------------------------------------------------*/
Sent* _new_sent()
{
    Sent* new_sent = (Sent*) malloc(sizeof(Sent));
    new_sent->words = NULL;
    new_sent->data_num = 0;
    return new_sent;
}

Para* _new_para()
{
    Para* new_para = (Para*) malloc(sizeof(Para));
    new_para->sents = NULL;
    new_para->data_num = 0;
    return new_para;
}

Doc* _new_doc()
{
    Doc* new_doc = (Doc*) malloc(sizeof(Doc));
    new_doc->paras = NULL;
    new_doc->data_num = 0;
    return new_doc;
}
/*-------------------------------------------------*/
/*-------------------------------------------------
                Append functions
-------------------------------------------------*/

void sent_append(char* new_word, Sent* sent)
{
    int curr_sent_len = ++sent->data_num;
    int word_len = strlen(new_word);
    char* tmp_word;
    sent->words = (char**) realloc(sent->words, curr_sent_len*sizeof(char*));
    if (sent->words){
        tmp_word = (char*) malloc(word_len+1);
        if (!tmp_word){
            release_sent(sent);
            exit(1);
        }
        strcpy(tmp_word, new_word);
        sent->words[curr_sent_len-1] = tmp_word;
    }
    else{
        release_sent(sent);
        exit(1);
    }
}

void para_append(Sent* new_sent, Para* para)
{
    int curr_para_len = ++para->data_num;
    para->sents = (Sent**) realloc(para->sents, curr_para_len*sizeof(Sent*));
    if (para->sents){
        para->sents[curr_para_len-1] = new_sent;
    }else{
        release_sent(new_sent);
        release_para(para);
        exit(1);
    }
}

void doc_append(Para* new_para, Doc* doc)
{
    int curr_doc_len = ++doc->data_num;
    doc->paras = (Para**) realloc(doc->paras, curr_doc_len*sizeof(Para*));
    if (doc->paras){
        doc->paras[curr_doc_len-1] = new_para;
    }
    else{
        release_para(new_para);
        release_doc(doc);
        exit(1);
    }
}

/*-------------------------------------------------
                Release functions
-------------------------------------------------*/
void release_sent(Sent* sent)
{
    int i;
    for (i = 0; i < sent->data_num; i++){
        free(sent->words[i]);
    }
    free(sent->words);
    free(sent);
}

void release_para(Para* para)
{
    int i;
    for (i = 0; i < para->data_num; i++){
        release_sent(para->sents[i]);
    }
    free(para->sents);
    free(para);
}

void release_doc(Doc* doc)
{
    int i;
    for (i=0; i < doc->data_num; i++){
        release_para(doc->paras[i]);
    }
    free(doc->paras);
    free(doc);
}
/*-------------------------------------------------
                Information functions
-------------------------------------------------*/
void sent_info(Sent* sent)
{
    int i;
    printf("--<Object<Sent>at(%p)>\n", sent);
    for (i = 0; i < sent->data_num; i++){
        printf("---(%d): %s\n", i, sent->words[i]);
    }
}

void para_info(Para* para)
{
    int i;
    Sent* tmp_sent;
    printf("-<Object<Para>at(%p)>\n", para);
    for (i = 0; i < para->data_num; i++){
        tmp_sent = para->sents[i];
        sent_info(tmp_sent);
    }
}

void doc_info(Doc* doc)
{
    int i;
    Para* tmp_para;
    printf("<Object<Doc>at(%p)>\n", doc);
    for (i = 0; i < doc->data_num; i++){
        tmp_para = doc->paras[i];
        para_info(tmp_para);
    }
}
