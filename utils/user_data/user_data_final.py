import requests
import json
import abc

class UserData(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self):
        pass

class Reader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass


class UserDataFromRequest(UserData):

    def __init__(self, profile_id: str):
        self.profile_id = profile_id

    def get(self):
        req = requests.get('<user-details-url>')
        status_code = req.status_code

        if status_code != 200:
            print(f'Error getting user details. Status Code: {status_code}')
            return None

        user_details = req.json()

        return user_details


class UserDataFromFile(UserData):

    def __init__(self, profile_id: str):
        self.profile_id = profile_id

    def get(self):
        return self.read()

    def read(self):
        return {
            'PXA5IVtq9QRwWQKduJKTQSdI70EvhFj8w5ql3UgI': {
                'about': 'Hello',
                'app': 'PXA5IVtq9QRwWQKduJKTQSdI70EvhFj8w5ql3UgI',
                'badges': [
                    {
                        'en': 'Online Learning Instructor Badge',
                        'es': 'Insignia de Docente para el Aprendizaje Online',
                        'pt': 'Medalha de facilitador de aprendizagem on-line'
                    },
                    {
                        'en': 'Blended Learning Designer Badge',
                        'es': 'Insignia de Diseñador de Aprendizaje Blended',
                        'pt': 'Medalha de designer de aprendizagem semipresencial'
                    },
                    {
                        'en': 'Blended Learning Instructor Badge',
                        'es': 'Insignia de Docente para el Aprendizaje Blended',
                        'pt': 'Medalha de facilitador de aprendizagem semipresencial'
                    },
                    {
                        'en': 'Online Learning Developer Badge',
                        'es': 'Insignia de Desarrollador de Aprendizaje Online',
                        'pt': 'Medalha de desenvolvedor de aprendizagem on-line'
                    },
                    {
                        'en': 'Online Learning Designer Badge',
                        'es': 'Insignia de Diseñador de Aprendizaje Online',
                        'pt': 'Medalha de designer de aprendizagem on-line'
                    }
                ],
                'collaboration_interests': [
                    'TEACHING_PROJECTS',
                    'RESEARCH_PROJECTS',
                    'MENTOR'
                ],
                'department': 'Computer Science',
                'doc_id': '846eab98-0950-4da3-84c8-ff72d7fae97f',
                'email': 'cristian.turcios@laureate.net',
                'english_proficiency': '',
                'field_of_study': 'Computer science',
                'first_name': 'Cristian',
                'followers': [
                    '9651d769-4e32-413c-b19a-bd42d998bfc6',
                    '65434b0f-14a6-434b-96f1-e490542b5160',
                    '50911353-eee0-4ba8-b61d-b32fb846acbc',
                    '23efc1ef-bc52-42bd-9a50-d21c9a82d067',
                    '9f29b961-53d5-49ac-bc39-58fe95be270e',
                    '8b22e54a-44d4-45a2-9217-db462501b64f',
                    'cdb2cc6a-b87b-4f78-aff5-c3138021ffcc',
                    'c28c37e0-8329-4d66-b83f-2da71f56ebc6',
                    'f746b49b-3b89-4832-be3f-441e584c7a2a'
                ],
                'following': [
                    'e4a7f311-69b8-42f4-b49a-78d17819b7aa',
                    'e2cfb87f-13a6-4f5f-bf54-e52a2d9503f0',
                    '5edad98f-4e39-4538-b49a-86b1f160dc21',
                    '9959ef2d-1293-41fa-bf97-2b530dd8404c',
                    '16e5a1bb-8344-462f-a68a-1eb7daa83218',
                    'eaf745dc-d102-43f0-95f5-45f96ae784c5',
                    '7eb4d5fb-c11f-4c7a-9e4b-27c3179b29c8',
                    'ebde4466-cd2d-4f1c-95d1-7fbbce0af834',
                    '65434b0f-14a6-434b-96f1-e490542b5160',
                    '9f29b961-53d5-49ac-bc39-58fe95be270e',
                    'c28c37e0-8329-4d66-b83f-2da71f56ebc6'
                ],
                'highest_credential': 'MASTER',
                'in_language_buddies': True,
                'interests': [
                    36,
                    34,
                    9,
                    10,
                    124,
                    121,
                    116,
                    49,
                    141
                ],
                'isoffice365': True,
                'language': 'English',
                'language_short': 'en',
                'last_name': 'Turcios',
                'location_en': 'Italy',
                'location_es': 'Italia',
                'location_id': '13',
                'location_pt': 'Itália',
                'native_languages': [
                    'Arabic_Egyptian_Spoken',
                    'Arabic_North_Levantine_Spoken'
                ],
                'passport_active': True,
                'phone': '+504 97354332',
                'picture': 'https://lh3.googleusercontent.com/DuILWqjfsfM2ZI-azo2iUi2egt1Wac0CZvcROKEEcKlniG1kJ7BqFG1ao1fhZ9l0HYYaCkP42cK5Cou2zwnfo7_U3_wi91DvwxI',
                'profile_id': '846eab98-0950-4da3-84c8-ff72d7fae97f',
                'profile_privacy': 'private',
                'region_en': 'Europe',
                'region_es': 'Europa',
                'region_pt': 'Europa',
                'role': 'ALUMNI',
                'skills_languages': [
                    'Arabic_Egyptian_Spoken',
                    'Arabic_Moroccan_Spoken',
                    'Arabic_Saidi_Spoken',
                    'Arabic_Tunisian_Spoken',
                    'Arabic_Najdi_Spoken',
                    'Arabic_North_Levantine_Spoken',
                    'Arabic_Mesopotamian_Spoken'
                ],
                'stamps': [
                    'connections'
                ],
                'university': '13',
                'university_acronym': 'Domus',
                'university_name': 'Domus Academy',
                'work_experience': [
                    'Passport Created',
                    'sdfg',
                    'prueba'
                ]
            },
            'dtQrvgVlFP2VWV5IpTGZP5w179Wf9lad95vh9JHI': {
                'about': 'Hello',
                'app': 'dtQrvgVlFP2VWV5IpTGZP5w179Wf9lad95vh9JHI',
                'badges': [],
                'collaboration_interests': [
                    'TEACHING_PROJECTS',
                    'RESEARCH_PROJECTS',
                    'MENTOR'
                ],
                'department': 'Computer Science',
                'doc_id': '846eab98-0950-4da3-84c8-ff72d7fae97f',
                'email': 'cristian.turcios@laureate.net',
                'english_proficiency': 'Native',
                'field_of_study': 'Computer science',
                'first_name': 'Cristian',
                'followers': [
                    '9651d769-4e32-413c-b19a-bd42d998bfc6',
                    '65434b0f-14a6-434b-96f1-e490542b5160',
                    '50911353-eee0-4ba8-b61d-b32fb846acbc',
                    '23efc1ef-bc52-42bd-9a50-d21c9a82d067',
                    '9f29b961-53d5-49ac-bc39-58fe95be270e',
                    '8b22e54a-44d4-45a2-9217-db462501b64f',
                    'cdb2cc6a-b87b-4f78-aff5-c3138021ffcc',
                    'c28c37e0-8329-4d66-b83f-2da71f56ebc6',
                    'f746b49b-3b89-4832-be3f-441e584c7a2a'
                ],
                'following': [
                    'e4a7f311-69b8-42f4-b49a-78d17819b7aa',
                    'e2cfb87f-13a6-4f5f-bf54-e52a2d9503f0',
                    '5edad98f-4e39-4538-b49a-86b1f160dc21',
                    '9959ef2d-1293-41fa-bf97-2b530dd8404c',
                    '16e5a1bb-8344-462f-a68a-1eb7daa83218',
                    'eaf745dc-d102-43f0-95f5-45f96ae784c5',
                    '7eb4d5fb-c11f-4c7a-9e4b-27c3179b29c8',
                    'ebde4466-cd2d-4f1c-95d1-7fbbce0af834',
                    '65434b0f-14a6-434b-96f1-e490542b5160',
                    '9f29b961-53d5-49ac-bc39-58fe95be270e',
                    'c28c37e0-8329-4d66-b83f-2da71f56ebc6'
                ],
                'highest_credential': 'MASTER',
                'in_language_buddies': True,
                'interests': [
                    92,
                    5
                ],
                'isoffice365': True,
                'language': 'English',
                'language_short': 'en',
                'last_name': 'Turcios',
                'location_en': 'Italy',
                'location_es': 'Italia',
                'location_id': '13',
                'location_pt': 'Itália',
                'native_languages': [
                    'English',
                    'Amharic'
                ],
                'passport_active': True,
                'phone': '+504 97354332',
                'picture': 'https://lh3.googleusercontent.com/DuILWqjfsfM2ZI-azo2iUi2egt1Wac0CZvcROKEEcKlniG1kJ7BqFG1ao1fhZ9l0HYYaCkP42cK5Cou2zwnfo7_U3_wi91DvwxI',
                'profile_id': '846eab98-0950-4da3-84c8-ff72d7fae97f',
                'profile_privacy': 'private',
                'region_en': 'Europe',
                'region_es': 'Europa',
                'region_pt': 'Europa',
                'role': 'ALUMNI',
                'skills_languages': [
                    'English',
                    'Portuguese',
                    'Spanish',
                    'Amharic'
                ],
                'stamps': [
                    'connections',
                    'masters_of_storytelling',
                    'episode-one',
                    'adapter',
                    'problemsolver',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'adapter',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver',
                    'problemsolver'
                ],
                'university': '13',
                'university_acronym': 'Domus',
                'university_name': 'Domus Academy',
                'work_experience': []
            }
        }
