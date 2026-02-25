import streamlit as st
import info
import pandas as pd

def introSection():
    st.image(info.border_picture, width = 600)
    st.header("Obscure Pop Culture Quiz")
    st.write("Answer these questions to determine how insane you are.")
    st.image(info.border_picture, width = 600)
introSection()

points = 0


def q1():
    st.subheader("Question 1")
    st.image(info.profile_picture, width = 200)
    who = st.radio(info.q1_label, info.q1_options, index=None) #NEW
    if who == "Will Wood":
        st.write("Correct!")
        global points
        points += 1
        return points
    else:
        if who != None:
            st.write("Incorrect. This is Will Wood!")
q1()

def q2():
    st.subheader("Question 2")
    st.image(info.daughter_picture, width = 350)
    daughter = st.selectbox(info.q2_label, info.q2_options, index=None, placeholder = "Daughter Status...") #NEW
    if daughter == "No":
        st.write("Correct!")
        st.write(info.daughter_explanation)
        global points
        points += 1
        return points
    else:
        if daughter != None:
            st.write("Incorrect.")
            st.write(info.daughter_explanation)
q2()

def q3():
    st.subheader("Question 3")
    st.image(info.eras_picture, width = 250)
    bands = st.text_input(info.q3_label, value=None, max_chars=6, placeholder="ex: abcdef") #NEW
    if bands == "cbdeaf":
        st.write("Correct! Will Wood's bands started producing music in this order: Jamface, Strange Thick, A Verbal Equinox, The Stereosexuals, Will Wood and the Tapeworms, Will Wood.")
        global points
        points += 2
        return points
    else:
        if bands != None:
            st.write("Incorrect. Will Wood's bands started producing music in this order: Jamface, Strange Thick, A Verbal Equinox, The Stereosexuals, Will Wood and the Tapeworms, Will Wood.")
q3()


def q4():
    st.subheader("Question 4")
    city = st.radio(info.q4_label, info.q4_options, index=None)
    if city == "Branson":
        st.write("Correct!")
        global points
        points += 1
        return points
    else:
        if city != None:
            st.write("Incorrect. Will Wood's last tour and live album was called 'Slouching Towards Branson'!")
q4()

def q5():
    st.subheader("Question 5")
    st.image(info.selfish_picture, width = 200)
    name = st.multiselect(info.q5_label, info.q5_options, default=None, max_selections=4) #NEW
    if "Soapbox Tao" in name:
        if "Neospace Government" in name:
            if "Checkmate Athiests!" in name:
                if "Strange and Profound" not in name:
                    if "Tree Fall" not in name:
                        st.write('Correct! The Will Wood and the Tapeworms hit song is entitled "The Song with Five Names, a.k.a. Soapbox Tao, a.k.a. Checkmate Atheists! a.k.a. Neospace Government, a.k.a. You Can Never Know".')
                        global points
                        points += 1
                        return points
    else:
        if name != None:
            st.write("Incorrect.")
q5()

def q6():
    st.subheader("Question 6")
    makeup = st.text_input(info.q6_label, value=None, placeholder="type symbol here [text]")
    if makeup != None:
        if "third eye" in makeup.lower():
            st.write("Correct!")
            global points
            points += 1
            return points
        else:
            st.write("Incorrect. Will Wood is known for his eccentric stage makeup containing a third eye.")
q6()
    

def q7():
    st.subheader("Question 7")
    st.image(info.world_picture, width = 200)
    topic = st.radio(info.q7_label, info.q7_options, index=None)
    if topic == "Guns":
        st.write("Correct!")
        global points
        points += 1
        return points
    else:
        if topic != None:
            st.write("Incorrect. Will Wood's Apocalypic Comedy podcast, \"Life in the World to Come\", is primarily about guns, including replacing body parts with guns, transforming into a gun, eating guns, and all sorts of essential things during the apocalypse.")
q7()


def q8():
    st.subheader("Question 8")
    name = st.multiselect(info.q8_label, info.q8_options, default=None, max_selections=3)
    if "Doug Kevendek" in name:
        if "The Real Will Wood Archive" in name:
            if "Will Wood Archive" not in name:
                if "Katy Armstead" not in name:
                    st.write("Correct! Doug Kevendek and The Real Will Wood Archive post obscure Will Wood content, including concert recordings and old/deleted music.")
                    global points
                    points += 2
                    return points
    else:
        if name != None:
            st.write("Incorrect. Doug Kevendek and The Real Will Wood Archive post obscure Will Wood content, including concert recordings and old/deleted music")
    
q8()


def insanityScore():
    st.image(info.border_picture, width = 600)
    st.header("And your score is...")
    global points
    insane = ""
    if points <=1:
        insane = "are confused."
    elif points <=4:
        insane = "have heard I/Me/Myself."
    elif points <= 7:
        insane = "are a Will Wood fan!"
    else:
        insane = "are insane!!!"
    st.write(f'You scored {points}/10. You {insane}')
    st.image(info.border_picture, width = 600)

insanityScore()




