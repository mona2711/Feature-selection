FROM huanjason/scikit-learn
#FROM jbei/scikit-learn
#RUN apk update
#RUN apk add make automake gcc g++ subversion python3-dev
RUN pip install --upgrade pip --user

ADD . .

RUN pip3 --no-cache-dir install -r requirement.txt --user

#RUN pip3 install numpy && \
#    pip3 install pandas

EXPOSE 5005

ENTRYPOINT [ "python", "api.py" ]