import os
import asposestoragecloud
import asposewordscloud
import asposewordscloud.models.requests

class Cloud_Training_Tasks(object):

    def __init__(self):
        api_client = asposewordscloud.ApiClient()
        api_client.configuration.host = 'https://api.aspose.cloud'
        api_client.configuration.api_key['api_key'] = '6e8a07bc42a0a634b7cf4b2d97b71b04'  # Put your appkey here
        api_client.configuration.api_key['app_sid'] = '3d30dc41-4f18-49e2-919e-704445248856'  # Put your appSid here

        # Same credentials for storage.
        self.storage_api = asposestoragecloud.StorageApi(
            asposestoragecloud.ApiClient(apiKey='6e8a07bc42a0a634b7cf4b2d97b71b04', appSid='3d30dc41-4f18-49e2-919e-704445248856'))  # Put your appKey and appSid here
        self.storage_api.api_client.configuration.base_url = 'https://api.aspose.cloud' + '/v1.1'
        self.words_api = asposewordscloud.WordsApi(api_client)

        ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
        self.dataFolder = os.path.join(ABSPATH, "Data")


    def Task1_HelloWorldConsole(self):
        # Task 1:  Print "Hello world!".
        print("Hello, World!")

    def Task2_DocToPdf(self):
        # Task 2:  Convert Doc to Pdf and upload to cloud.
        filename = 'Tech_Article_Viktor.doc'
        output_filename = 'Tech_Article_Viktor.pdf'
        filePath = os.path.join(self.dataFolder, filename)
        # Read the word document
        with open(filePath, 'rb') as f:
            fileData = f.read()
        file_upload_response = self.storage_api.put_create(filename, fileData)
        # Check if file uploaded successfully to Cloud Storage
        if (file_upload_response["Code"] == 200 and file_upload_response["Status"] == "OK"):
            save_options = asposewordscloud.PdfSaveOptionsData(save_format='pdf', file_name=output_filename)
            request = asposewordscloud.models.requests.PostDocumentSaveAsRequest(filename, save_options)
            result = self.words_api.post_document_save_as(request)

    def Task3_HelloWorldAW(self):
        # Task 3: Programmatically create a document, insert a paragraph with text Hello World, and save to cloud.
        fileName = "CreateDocument_out.docx"
        fileData = 'Hello, world!'
        # create doc on cloud and save string
        file_upload_response = self.storage_api.put_create(fileName, fileData)

    def Task4_JoinTwoDocuments(self):
        # Task 4:  Programmatically join two documents and save to disk.
        append_document_1 = 'TestFile.Destination.doc'
        append_document_2 = 'TestFile.Source.doc'
        dest_name = 'Joined_Document_out.doc'
        # Upload Main Document and "Documents to append" to cloud storage.
        for filename in [append_document_1, append_document_2]:
            filePath = os.path.join(self.dataFolder, filename)
            with open(filePath, 'rb') as f:
                fileData = f.read()
            file_upload_response = self.storage_api.put_create(filename, fileData)

        # Can be KeepSourceFormatting or UseDestinationStyles.
        doc_entry_1 = asposewordscloud.DocumentEntry(append_document_1,
                                                     'KeepSourceFormatting')
        doc_entry_2 = asposewordscloud.DocumentEntry(append_document_2,
                                                     'UseDestinationStyles')
        document_list = asposewordscloud.DocumentEntryList([doc_entry_2])

        request = asposewordscloud.models.requests.PostAppendDocumentRequest(append_document_1,
                                                                             document_list,
                                                                             dest_file_name=dest_name)
        result = self.words_api.post_append_document(request)

    def Task5_ReplaceTextOfBookmark(self):
        # Programmatically open the document with a bookmark, replace the bookmarked text, and save the new document to cloud.
        filename = 'Document_w_bookmark.doc'
        bookmark_name = 'Characteristics'
        body = asposewordscloud.BookmarkData(bookmark_name, 'This is a new bookmarked text.')
        dest_name = 'Document_new_bookmark_out.doc'

        filePath = os.path.join(self.dataFolder, filename)
        with open(filePath, 'rb') as f:
            fileData = f.read()

        file_upload_response = self.storage_api.put_create(filename, fileData)
        # Check if file uploaded successfully to Cloud Storage
        if (file_upload_response["Code"] == 200 and file_upload_response["Status"] == "OK"):
           request = asposewordscloud.models.requests.PostUpdateDocumentBookmarkRequest(filename, body,
                                                                                         bookmark_name,
                                                                                         dest_file_name=dest_name)
           result = self.words_api.post_update_document_bookmark(request)


mycloud = Cloud_Training_Tasks()
mycloud.Task1_HelloWorldConsole()
mycloud.Task2_DocToPdf()
mycloud.Task3_HelloWorldAW()
mycloud.Task4_JoinTwoDocuments()
mycloud.Task5_ReplaceTextOfBookmark()
print('Output files are successfully uploaded to cloud.')