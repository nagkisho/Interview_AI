from streamlit_extras.switch_page_button import switch_page
import streamlit as st
import pandas as pd
import random
import time
from Page1 import *
import streamlit as st
import os
import openai

openai.api_key = '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'


# st.set_page_config(initial_sidebar_state='collapsed')

if 'Domain' not in st.session_state:
    st.session_state['Domain'] = 'Empty'
if 'Interview' not in st.session_state:
    st.session_state['Interview'] = 'Empty'
if 'question' not in st.session_state:
    st.session_state['question'] = 0
if 'Start' not in st.session_state:
    st.session_state['Start'] = "Done"

if (st.session_state['Interview']=='True'):
    if (st.session_state['Domain']!='Empty'):
        df = pd.read_excel(r"C:\Users\dhishind\Desktop\GPT-FEEDBACK\GPT-FEEDBACK\All_questions.xlsx")
        skill = st.session_state['Domain']
        st.write("Interview for ",skill)
        nlist = list(range(0,len(df)))
        
        def interview_q(skill,n_q=7,df=df):
            qn = []
            Question = list(df[skill])
            nlist=list(range(0,len(df[skill])))
            for i in range(n_q):
                list1 = list(nlist)
                n = random.choice(list1)
                nlist = set(list1) - {n}
                # yield Question[n]
                qn.append(Question[n])
            return qn

        def hr_q(n_q=2,df=df):
            qn = []
            Question = list(df['HR'])
            nlist=list(range(0,len(df["HR"])))
            nlist = nlist[1:-1]
            for i in range(n_q):
                list1 = list(nlist)
                n = random.choice(list1)
                nlist = set(list1) - {n}
                # yield Question[n]
                qn.append(Question[n])
            return qn    

                # print(Question[n])
            # x = st.empty()
            # x.write(Question[n])
        q = hr_q()+interview_q(skill)
        q.append(list(df["HR"])[-1])
        q.insert(0,df["HR"][0])
        
        # count=0

        col1, col2,col3 = st.columns(3)
        with col1:
            pass
            # start = st.empty()
            # start_button = start.button("Start")
            # if start_button:
            #     st.session_state["Start"] = "True"
            #     start.empty()
        with col2:
            pass
        with col3:
            
            placeholder = st.empty()
            isclick = placeholder.button('Next')
        # ph1 = st.empty()
        # ph2 = st.empty()
        # col4, col5 = st.columns(2)
        # with col4:
        #     ph1.write(q[0])
        # with col5:
        #     video_html = """
        #         <video controls autoplay="true" >
        #         <source 
        #             src="C:/Users/araj18/Documents/Video GAN/Java_5.mp4"
        #             type="video/mp4" />
        #         </video>
        #         """
        #     ph2.markdown(video_html, unsafe_allow_html=True)     
    
        if isclick or st.session_state['question']==0 :
            # ph1.empty()
            # ph2.empty()
            x = st.session_state['question']
            if x>=11:
                st.write("Interview Complete")
                placeholder.empty()
                st.session_state['question']=-1
                st.session_state['Domain']='Empty'
            else:
                with st.form(key='columns_in_form'):
                    st.session_state['question']+=1
                    col6, col7 = st.columns(2)
                    with col6:
                        st.write(q[x])
                        def gpt3(texts):
                            # openai.api_key = os.environ["Secret"]
                        # openai.api_key = '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'#'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' #'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'
                            response = openai.Completion.create(
                            engine="text-davinci-002",
                            prompt= texts,     
                            max_tokens=750,
                            top_p=1,
                            frequency_penalty=0.0,          
                            presence_penalty=0.0,
                            stop = (";", "/*", "</code>"))
                            x = response.choices[0].text 
                            return x

                        userPrompt = st.text_area("Answer:")
                        submitButton = st.form_submit_button(label = 'Analyze')
                        if submitButton:
                            with open("feedback_fewshot.txt", "r") as file:
                                text_file = file.read()
                                        
                                r_prompt= text_file+ q[x] +userPrompt
                                #st.write(r_prompt)

                                recommedation = openai.Completion.create(
                                                    engine="text-davinci-003",
                                                    prompt = r_prompt,
                                                    max_tokens=1024,
                                                    n=1,
                                                    stop=None,
                                                    temperature=0.5,)
                                if recommedation['choices'][0]['text'] != "":  
                                                    st.write('Feedback:')
                                                    st.success(recommedation['choices'][0]['text'])


                with col7:
                    # import streamlit as st
                    # from audio_recorder_streamlit import audio_recorder

                    # audio_bytes = audio_recorder("Click to record", "Recording...")
                    # if audio_bytes:
                    #     st.audio(audio_bytes, format="audio/wav")
                    #     with open("C:/Users/dhishind/Desktop/IMP/DocumentsNib\audio_1.mp3", 'wb') as f:
                    #         f.write(audio_bytes)

                    video_html = """
                            <video controls autoplay="true">
                            <source 
                                        src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm"
                                        type="video/mp4" />
                            </video>

                        """
                    st.markdown(video_html, unsafe_allow_html=True)
            # st.session_state["Start"]="Done"
                    # st.video(r"C:\Users\araj18\Downloads\Java_5.mp4", format='video/mp4', start_time=0)
        # with open("file.txt", "r") as f:
        #     a = f.readline()  # starts as a string
        #     a = 0 if a == "" else int(a)
            
        # if isclick:
        #     a+=1
        #     with open("file.txt", "w") as f:
        #         f.truncate()
        #         f.write(f"{a}")
        #         # st.write(a)
        #         try:
        #             st.write(Question[q[a]])
        #         except:
        #             f.truncate(0)
        #             placeholder.empty()
        #             st.write("Interview Complete")
            # print(count)
            # st.write(count)
            # try:
            #     ques=next(q)
            #     print(ques)
            #     st.write(ques)
            # except:
            #     # placeholder.empty()
            #     st.write("Interview Complete")
            # else:
            #     time.sleep(10)
            #     placeholder.empty()
            #     x.empty()
        # 
        
    else:
        st.info("Please Select a skill domain to Interview")
    # st.session_state['Domain']='Empty'
else:
    st.info("Please Login to continue")