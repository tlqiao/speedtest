from backend.testcase.chains import devide_requirments,ask_question,summary_requirements
from backend.rag.retriever import query_question
import json

def gen_new_feature_list(original_feature,model_name,file_name_list):
        question = ask_question(original_feature)
        answer= query_question(question=question,chat_model=model_name,file_name_list=file_name_list)
        new_feature= summary_requirements(original_feature, answer,model_name=model_name)  
        result= {
        "original_feature": original_feature,
        "question": question,
        "answer": answer,
        "new_feature": new_feature
    }
        print("---here is new feature object---")
        print(json.dumps(result))
        return result

def get_devided_requirements (original_requirements,number_feature,model_name,search_file_list): 
        feature_list = devide_requirments(original_requirements=original_requirements, feature_number=number_feature,model_name=model_name)
        new_feature_list=[]
        for orginal_feature in feature_list:
                new_feature_list.append(gen_new_feature_list(original_feature=orginal_feature,model_name=model_name,file_name_list=search_file_list))
        return new_feature_list


def summary_devided_requirement_together(devided_features):
         return '\n\nDevided Feature\n\n'.join(obj['new_feature'] for obj in devided_features)