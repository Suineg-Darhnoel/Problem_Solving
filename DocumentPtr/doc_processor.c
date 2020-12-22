#include "doc_processor.h"
/* 
   word < sentence < paragraph < doc
*/

int* part_delim_indices(char* full_text, char delim, int* list_len)
{
    /* NOTE!:
        1. Case: Paragraph
            The last paragraph does not end with a newline 
            because of the above reasn head offset and tail offset are included
            ex: "I\nYou\nWe" -> [_0_, 1, 5, _8_]
            where -1 and 8 (length of the "I\nYou\nWe") are the offsets
        2. Case: Word
            The last word in a sentence does not end with a space " " 
            because of the above reason head offset and tail offset are included
            ex: "I love you" -> [_0_, 1, 6, _10_]
            where -1 and 10 (length of the "I love you") are the offsets
    */
    int i;
    int text_len = strlen(full_text);
    int* part_indices = (int*) malloc(sizeof(int));
    int array_len = 1;
    part_indices[array_len-1] = -1;

    // record every delimiter's position
    for (i=0, array_len=1; i<text_len; i++){
        if (full_text[i] == delim){
            array_len++;
            part_indices = (int*) realloc(
                part_indices, (array_len)*sizeof(int));
            part_indices[array_len-1] = i;
        }
    }
    
    if (delim != '.'){
        array_len++;
        part_indices = (int*) realloc(
            part_indices, (array_len)*sizeof(int));
        part_indices[array_len-1] = text_len;
    }

    *list_len = array_len;

    return part_indices;
}

char* trim_text(char* text, int fr, int to)
{
    assert(fr >= 0 || to >= 0 || to >= fr);

    int trim_len = to-fr+1;
    char* text_part = (char*) malloc(trim_len+1);
    strncpy(text_part, &text[fr], trim_len);
    text_part[trim_len-1] = '\0';

    return text_part;
}

char* small_section(
        char* bg_section_text,
        int* delim_indices,
        int index
    )
{
    char* sm_section_text = trim_text(
            bg_section_text,
            delim_indices[index]+1,
            delim_indices[index+1]
        );

    return sm_section_text;
}

void print_line(int num_of_char, char c)
{
    for (int i=0; i<num_of_char; i++){
        printf("%c", c);
    }
    puts("");
}

void show_text_structure(
        char* text,
        int tag )
{
    char TAG_OPEN[20];
    char TAG_CLOSE[20];
    enum tags{PARA, SENT, WORD};

    switch (tag){
        case WORD:
            strcpy(TAG_OPEN, "<Word>");
            strcpy(TAG_CLOSE, "</Word>");
            break;
        case SENT:
            strcpy(TAG_OPEN, "<Sent>");
            strcpy(TAG_CLOSE, "</Sent>");
            break;
        default:
            strcpy(TAG_OPEN, "<Para>");
            strcpy(TAG_CLOSE, "</Para>");
    }
    printf("%s", TAG_OPEN);

    printf("%s%s\n", text, TAG_CLOSE);
}


Doc* get_document(char* text)
{
    // Initialize a Doc data structure
    Doc* new_doc_struct = _new_doc();
    Para* new_para_struct = _new_para();
    Sent* tmp_sent_struct;

    int para_indices_len;
    int* para_indices = part_delim_indices(
            text, '\n', &para_indices_len);
    for (int i=0; i<para_indices_len-1; i++){
        print_line(20, '*');
        char* tmp_para = small_section(text, para_indices, i);

        int sent_indices_len;
        int* sent_indices = part_delim_indices(
            tmp_para, '.', &sent_indices_len);
        for (int j=0; j<sent_indices_len-1; j++){
            char* tmp_sent = small_section(tmp_para, sent_indices, j);
            tmp_sent_struct = _new_sent();

            int word_indices_len;
            int* word_indices = part_delim_indices(
                tmp_sent, ' ', &word_indices_len);
            for (int k=0; k<word_indices_len-1; k++){
                char* tmp_word = small_section(tmp_sent, word_indices, k);
                sent_append(tmp_word, tmp_sent_struct);
                /* show_text_structure(tmp_word, 2); */
                free(tmp_word);
            }
            /* show_text_structure(tmp_sent, 1); */
            free(tmp_sent);
            para_append(tmp_sent_struct, new_para_struct);
            free(word_indices);
        }
        /* show_text_structure(tmp_para, 0); */
        free(tmp_para);
        free(sent_indices);
    }
    free(para_indices);

    doc_append(new_para_struct, new_doc_struct);
    return new_doc_struct;
}

