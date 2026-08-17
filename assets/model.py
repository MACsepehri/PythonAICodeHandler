import json
import os
import stackexchange

class Stackoverflow:
    def __init__(self):
        self.so = stackexchange.Site(stackexchange.StackOverflow)
        self.so.impose_throttling = True

    def search(self, Input, max_results=10, sort="relevance"):
        try:
            sort_map = {
                "relevance": "relevance",
                "creation": "creation",
                "votes": "votes"
            }
            sort_param = sort_map.get(sort, "relevance")
            
            questions = self.so.questions(
                q=Input,
                sort=sort_param,
                pagesize=min(max_results, 100)
            )
            
            questions = questions.fetch()
            
            if questions:
                results = []
                for q in questions[:max_results]:
                    results.append({
                        'title': q.title,
                        'link': f"https://stackoverflow.com/questions/{q.id}",
                        'score': q.score,
                        'answer_count': q.answer_count,
                        'tags': q.tags
                    })
                return results
            else:
                print("No Stack Overflow results found")
                return None
                
        except Exception as e:
            print(f"Error searching Stack Overflow: {e}")
            return None

class W3Schools:
    def __init__(self):
        self.all_tutorials = {
            "python": {
                "default": [
                    {"title": "Python Tutorial", "link": "https://www.w3schools.com/python/"}
                ],
                "list": [
                    {"title": "Python Lists", "link": "https://www.w3schools.com/python/python_lists.asp"},
                    {"title": "Python List Methods", "link": "https://www.w3schools.com/python/python_ref_list.asp"}
                ],
                "reverse": [
                    {"title": "Python Reverse List", "link": "https://www.w3schools.com/python/ref_list_reverse.asp"}
                ],
                "csv": [
                    {"title": "Python CSV", "link": "https://www.w3schools.com/python/python_csv.asp"}
                ],
                "json": [
                    {"title": "Python JSON", "link": "https://www.w3schools.com/python/python_json.asp"}
                ],
                "requests": [
                    {"title": "Python Requests", "link": "https://www.w3schools.com/python/python_requests.asp"}
                ],
                "exception": [
                    {"title": "Python Try Except", "link": "https://www.w3schools.com/python/python_try_except.asp"}
                ],
                "class": [
                    {"title": "Python Classes", "link": "https://www.w3schools.com/python/python_classes.asp"},
                    {"title": "Python Inheritance", "link": "https://www.w3schools.com/python/python_inheritance.asp"}
                ],
                "decorator": [
                    {"title": "Python Decorators", "link": "https://www.w3schools.com/python/python_decorators.asp"}
                ],
                "lambda": [
                    {"title": "Python Lambda", "link": "https://www.w3schools.com/python/python_lambda.asp"}
                ],
                "regex": [
                    {"title": "Python Regex", "link": "https://www.w3schools.com/python/python_regex.asp"}
                ],
                "datetime": [
                    {"title": "Python Datetime", "link": "https://www.w3schools.com/python/python_datetime.asp"}
                ],
                "file": [
                    {"title": "Python File Handling", "link": "https://www.w3schools.com/python/python_file_handling.asp"}
                ],
                "django": [
                    {"title": "Python Django", "link": "http://w3schools.com/django/"}
                ],
                "mysql": [
                    {"title": "Python MySQL", "link": "https://www.w3schools.com/python/python_mysql_getstarted.asp"}
                ]
            },
            "javascript": {
                "default": [
                    {"title": "JavaScript Tutorial", "link": "https://www.w3schools.com/js/"}
                ],
                "array": [
                    {"title": "JavaScript Arrays", "link": "https://www.w3schools.com/js/js_arrays.asp"},
                    {"title": "JavaScript Array Methods", "link": "https://www.w3schools.com/js/js_array_methods.asp"}
                ],
                "map": [
                    {"title": "JavaScript Array map()", "link": "https://www.w3schools.com/jsref/jsref_map.asp"}
                ],
                "fetch": [
                    {"title": "JavaScript Fetch API", "link": "https://www.w3schools.com/js/js_api_fetch.asp"}
                ],
                "promise": [
                    {"title": "JavaScript Promises", "link": "https://www.w3schools.com/js/js_promise.asp"}
                ],
                "async": [
                    {"title": "JavaScript Async/Await", "link": "https://www.w3schools.com/js/js_async.asp"}
                ],
                "dom": [
                    {"title": "JavaScript DOM", "link": "https://www.w3schools.com/js/js_htmldom.asp"}
                ],
                "event": [
                    {"title": "JavaScript Events", "link": "https://www.w3schools.com/js/js_events.asp"}
                ],
                "arrow": [
                    {"title": "JavaScript Arrow Functions", "link": "https://www.w3schools.com/js/js_arrow_functions.asp"}
                ],
                "class": [
                    {"title": "JavaScript Classes", "link": "https://www.w3schools.com/js/js_classes.asp"}
                ],
                "localstorage": [
                    {"title": "JavaScript LocalStorage", "link": "https://www.w3schools.com/js/js_api_web_storage.asp"}
                ],
                "json": [
                    {"title": "JavaScript JSON", "link": "https://www.w3schools.com/js/js_json_intro.asp"}
                ],
                "timeout": [
                    {"title": "JavaScript setTimeout", "link": "https://www.w3schools.com/jsref/jsref_settimeout.asp"}
                ],
                "filter": [
                    {"title": "JavaScript Array filter()", "link": "https://www.w3schools.com/jsref/jsref_filter.asp"}
                ],
                "reduce": [
                    {"title": "JavaScript Array reduce()", "link": "https://www.w3schools.com/jsref/jsref_reduce.asp"}
                ],
                "spread": [
                    {"title": "JavaScript Spread Operator", "link": "https://www.w3schools.com/js/js_operators.asp"}
                ],
                "template": [
                    {"title": "JavaScript Template Literals", "link": "https://www.w3schools.com/js/js_string_templates.asp"}
                ],
                "module": [
                    {"title": "JavaScript Modules", "link": "https://www.w3schools.com/js/js_modules.asp"}
                ],
                "try": [
                    {"title": "JavaScript Try Catch", "link": "https://www.w3schools.com/js/js_errors.asp"}
                ],
                "closure": [
                    {"title": "JavaScript Closures", "link": "https://www.w3schools.com/js/js_function_closures.asp"}
                ],
                "hoisting": [
                    {"title": "JavaScript Hoisting", "link": "https://www.w3schools.com/js/js_hoisting.asp"}
                ],
                "event loop": [
                    {"title": "JavaScript Event Loop", "link": "https://www.w3schools.com/js/js_events.asp"}
                ],
                "callback": [
                    {"title": "JavaScript Callbacks", "link": "https://www.w3schools.com/js/js_callbacks.asp"}
                ]
            },
            "html": {
                "default": [
                    {"title": "HTML Tutorial", "link": "https://www.w3schools.com/html/"},
                    {"title": "HTML Div Tag", "link": "https://www.w3schools.com/tags/tag_div.asp"},
                    {"title": "HTML Forms", "link": "https://www.w3schools.com/html/html_forms.asp"},
                    {"title": "HTML Tables", "link": "https://www.w3schools.com/html/html_tables.asp"}
                ],
                "center": [
                    {"title": "HTML Center", "link": "https://www.w3schools.com/tags/tag_center.asp"}
                ],
                "form": [
                    {"title": "HTML Form Input Types", "link": "https://www.w3schools.com/html/html_form_input_types.asp"}
                ],
                "table": [
                    {"title": "HTML Table", "link": "https://www.w3schools.com/html/html_tables.asp"}
                ],
                "div": [
                    {"title": "HTML Div", "link": "https://www.w3schools.com/tags/tag_div.asp"},
                    {"title": "HTML Span", "link": "https://www.w3schools.com/tags/tag_span.asp"}
                ],
                "semantic": [
                    {"title": "HTML Semantic Elements", "link": "https://www.w3schools.com/html/html5_semantic_elements.asp"}
                ],
                "canvas": [
                    {"title": "HTML Canvas", "link": "https://www.w3schools.com/html/html5_canvas.asp"}
                ],
                "video": [
                    {"title": "HTML Video", "link": "https://www.w3schools.com/html/html5_video.asp"},
                    {"title": "HTML Audio", "link": "https://www.w3schools.com/html/html5_audio.asp"}
                ],
                "doctype": [
                    {"title": "HTML Doctype", "link": "https://www.w3schools.com/tags/tag_doctype.asp"},
                    {"title": "HTML Meta Tags", "link": "https://www.w3schools.com/tags/tag_meta.asp"}
                ],
                "bootstrap": [
                    {"title": "HTML Bootstrap Grid", "link": "https://www.w3schools.com/bootstrap5/bootstrap_grid_system.php"}
                ],
                "iframe": [
                    {"title": "HTML Iframe", "link": "https://www.w3schools.com/html/html_iframe.asp"}
                ],
                "link": [
                    {"title": "HTML Link Tag", "link": "https://www.w3schools.com/tags/tag_link.asp"},
                    {"title": "HTML Script Tag", "link": "https://www.w3schools.com/tags/tag_script.asp"}
                ]
            },
            "css": {
                "default": [
                    {"title": "CSS Tutorial", "link": "https://www.w3schools.com/css/"},
                    {"title": "CSS Flexbox", "link": "https://www.w3schools.com/css/css3_flexbox.asp"},
                    {"title": "CSS Grid", "link": "https://www.w3schools.com/css/css_grid.asp"},
                    {"title": "CSS Selectors", "link": "https://www.w3schools.com/css/css_selectors.asp"}
                ],
                "flexbox": [
                    {"title": "CSS Flexbox", "link": "https://www.w3schools.com/css/css3_flexbox.asp"}
                ],
                "grid": [
                    {"title": "CSS Grid", "link": "https://www.w3schools.com/css/css_grid.asp"}
                ],
                "media": [
                    {"title": "CSS Media Queries", "link": "https://www.w3schools.com/css/css_rwd_mediaqueries.asp"}
                ],
                "animation": [
                    {"title": "CSS Animations", "link": "https://www.w3schools.com/css/css3_animations.asp"}
                ],
                "position": [
                    {"title": "CSS Position", "link": "https://www.w3schools.com/css/css_positioning.asp"}
                ],
                "box": [
                    {"title": "CSS Box Model", "link": "https://www.w3schools.com/css/css_boxmodel.asp"}
                ],
                "variable": [
                    {"title": "CSS Variables", "link": "https://www.w3schools.com/css/css3_variables.asp"}
                ],
                "pseudo": [
                    {"title": "CSS Pseudo-classes", "link": "https://www.w3schools.com/css/css_pseudo_classes.asp"},
                    {"title": "CSS Pseudo-elements", "link": "https://www.w3schools.com/css/css_pseudo_elements.asp"}
                ],
                "transition": [
                    {"title": "CSS Transitions", "link": "https://www.w3schools.com/css/css3_transitions.asp"},
                    {"title": "CSS Transform", "link": "https://www.w3schools.com/css/css3_2dtransforms.asp"}
                ],
                "z-index": [
                    {"title": "CSS z-index", "link": "https://www.w3schools.com/css/css_z-index.asp"}
                ]
            },
            "sql": {
                "default": [
                    {"title": "SQL Tutorial", "link": "https://www.w3schools.com/sql/"},
                    {"title": "SQL SELECT", "link": "https://www.w3schools.com/sql/sql_select.asp"}
                ],
                "join": [
                    {"title": "SQL JOIN", "link": "https://www.w3schools.com/sql/sql_join.asp"}
                ],
                "group": [
                    {"title": "SQL GROUP BY", "link": "https://www.w3schools.com/sql/sql_groupby.asp"},
                    {"title": "SQL HAVING", "link": "https://www.w3schools.com/sql/sql_having.asp"}
                ],
                "insert": [
                    {"title": "SQL INSERT", "link": "https://www.w3schools.com/sql/sql_insert.asp"}
                ],
                "update": [
                    {"title": "SQL UPDATE", "link": "https://www.w3schools.com/sql/sql_update.asp"},
                    {"title": "SQL DELETE", "link": "https://www.w3schools.com/sql/sql_delete.asp"}
                ],
                "create": [
                    {"title": "SQL CREATE TABLE", "link": "https://www.w3schools.com/sql/sql_create_table.asp"},
                    {"title": "SQL PRIMARY KEY", "link": "https://www.w3schools.com/sql/sql_primarykey.asp"}
                ],
                "foreign": [
                    {"title": "SQL FOREIGN KEY", "link": "https://www.w3schools.com/sql/sql_foreignkey.asp"}
                ],
                "index": [
                    {"title": "SQL Index", "link": "https://www.w3schools.com/sql/sql_create_index.asp"}
                ],
                "subquery": [
                    {"title": "SQL Subquery", "link": "https://www.w3schools.com/sql/sql_subquery.asp"}
                ],
                "distinct": [
                    {"title": "SQL DISTINCT", "link": "https://www.w3schools.com/sql/sql_distinct.asp"}
                ],
                "order": [
                    {"title": "SQL ORDER BY", "link": "https://www.w3schools.com/sql/sql_orderby.asp"},
                    {"title": "SQL LIMIT", "link": "https://www.w3schools.com/sql/sql_limit.asp"}
                ],
                "like": [
                    {"title": "SQL LIKE", "link": "https://www.w3schools.com/sql/sql_like.asp"}
                ],
                "case": [
                    {"title": "SQL CASE", "link": "https://www.w3schools.com/sql/sql_case.asp"}
                ],
                "union": [
                    {"title": "SQL UNION", "link": "https://www.w3schools.com/sql/sql_union.asp"},
                    {"title": "SQL INTERSECT", "link": "https://www.w3schools.com/sql/sql_intersect.asp"},
                    {"title": "SQL EXCEPT", "link": "https://www.w3schools.com/sql/sql_except.asp"}
                ],
                "date": [
                    {"title": "SQL Date Functions", "link": "https://www.w3schools.com/sql/sql_dates.asp"}
                ],
                "aggregate": [
                    {"title": "SQL Aggregate Functions", "link": "https://www.w3schools.com/sql/sql_aggregate_functions.asp"}
                ],
                "procedure": [
                    {"title": "SQL Stored Procedures", "link": "https://www.w3schools.com/sql/sql_stored_procedures.asp"}
                ],
                "trigger": [
                    {"title": "SQL Triggers", "link": "https://www.w3schools.com/sql/sql_triggers.asp"}
                ],
                "view": [
                    {"title": "SQL Views", "link": "https://www.w3schools.com/sql/sql_view.asp"}
                ],
                "transaction": [
                    {"title": "SQL Transactions", "link": "https://www.w3schools.com/sql/sql_transactions.asp"}
                ],
                "window": [
                    {"title": "SQL Window Functions", "link": "https://www.w3schools.com/sql/sql_window_functions.asp"}
                ]
            }
        }
    
    def search(self, Input):
        Input_lower = Input.lower()
        results = []
        added_links = set()
        
        for topic, tutorials in self.all_tutorials.items():
            if topic in Input_lower:
                matched = False
                for keyword, tut_list in tutorials.items():
                    if keyword != "default" and keyword in Input_lower:
                        for tut in tut_list:
                            if tut["link"] not in added_links:
                                results.append(tut)
                                added_links.add(tut["link"])
                        matched = True
                        
                if not matched and "default" in tutorials:
                    for tut in tutorials["default"]:
                        if tut["link"] not in added_links:
                            results.append(tut)
                            added_links.add(tut["link"])
        
        if not results:
            results = self.all_tutorials.get("html", {}).get("default", [])
        
        return results

    @property
    def tutorials(self):
        return self.all_tutorials

class TrainerModel:
    def __init__(self):
        self.data = []
        self.stackoverflow = Stackoverflow()
        self.w3school = W3Schools()
        self.training_count = 0
        self.last_query = None
        self.cache = {}
        self.failed_queries = []
    
    def get_params(self):
        return {
            'data_count': len(self.data),
            'training_count': self.training_count,
            'last_query': self.last_query,
            'has_data': bool(self.data)
        }
    
    def validInput(self, Input: str):
        if Input == "":
            return False
        elif Input == " ":
            return False
        elif Input.replace(" ", "") == "":
            return False
        return True

    def train(self, data):
        if data not in self.data:
            self.data.append(data)
            self.training_count += 1
            self.last_query = data if data else None 

    def find(self, inp):
        for val in self.data:
            if inp.lower() in val.lower():
                return True
        return False

    def process(self, Input: str, Data: list = []):
        result = {
            'stackoverflow_links': [],
            'stackoverflow_codes': [],
            'w3schools_links': [],
            'raw_response': ""
        }
        
        if not self.validInput(Input):
            result['raw_response'] = "Please enter a valid input."
            return result

        if Data == []:
            if self.find(Input):
                for val in self.data:
                    if Input.lower() == val.lower():
                        result['raw_response'] = val
                        return result
            
            if Input in self.cache:
                print(f"Using cached result for: {Input}")
                formatted_response = self.cache[Input]
                result['raw_response'] = formatted_response
                self.train(formatted_response)
                return result
            
            stackoverflow_results = self.stackoverflow.search(Input)
            
            if stackoverflow_results:
                for idx, item in enumerate(stackoverflow_results[:5], 1):
                    result['stackoverflow_links'].append({
                        'title': item.get('title', 'Untitled'),
                        'link': item.get('link', '#')
                    })
            else:
                result['raw_response'] += "No Stack Overflow results found.\n\n"
            
            w3school_results = self.w3school.search(Input)
            if w3school_results:
                for item in w3school_results[:5]:
                    result['w3schools_links'].append({
                        'title': item['title'],
                        'link': item['link']
                    })
            else:
                result['raw_response'] += "No W3Schools results found.\n"
            
            formatted_response = self._format_response(result)
            result['raw_response'] = formatted_response
            
            if formatted_response and formatted_response != "No results found." and not formatted_response.startswith("No Stack Overflow"):
                self.cache[Input] = formatted_response
                self.train(formatted_response)
                print(f"Successfully learned: {Input}")
            else:
                self.cache[Input] = formatted_response
                print(f"No results to learn for: {Input}")
            
            return result
        else:
            l = []
            with open(f"data/main.json", "r") as file:
                content = json.load(file)["list"]
                for con in content:
                    if Input.lower() in con.lower():
                        l.append(con)
            return {"raw_response": l}

    def save(self, data, name="main"):
        if isinstance(data, str):
            data_list = [data]
        elif isinstance(data, list):
            data_list = data
        else:
            print(f"Unsupported data type: {type(data)}")
            return
        
        os.makedirs("data", exist_ok=True)
        
        file_path = f"data/{name}.json"
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                file_data = json.load(file)
                if not isinstance(file_data, dict) or "list" not in file_data:
                    file_data = {"list": []}
        except (FileNotFoundError, json.JSONDecodeError):
            file_data = {"list": []}
        
        existing_items = set(item.lower() for item in file_data["list"])
        new_items = []
        
        for item in data_list:
            if item.lower() not in existing_items:
                new_items.append(item)
                existing_items.add(item.lower())
        
        if new_items:
            file_data["list"].extend(new_items)
            
            try:
                with open(file_path, "w", encoding="utf-8") as wFile:
                    json.dump(file_data, wFile, indent=2, ensure_ascii=False)
                print(f"Added {len(new_items)} new items to {name}.json")
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print(f"No new items to add to {name}.json")
    
    def _format_response(self, result):
        formatted = ""
        
        if result['stackoverflow_links']:
            formatted += "Stack Overflow Results:\n"
            for idx, link in enumerate(result['stackoverflow_links'], 1):
                formatted += f"  {idx}. {link['title']}: {link['link']}\n"
            
            if result['stackoverflow_codes']:
                formatted += "\nCode Examples:\n"
                for idx, code in enumerate(result['stackoverflow_codes'], 1):
                    formatted += f"  Code {idx} (Language: {code['language']}):\n"
                    formatted += f"    {code['code'][:200]}...\n"
        
        if result['w3schools_links']:
            formatted += "\nW3Schools Tutorials:\n"
            for idx, link in enumerate(result['w3schools_links'], 1):
                formatted += f"  {idx}. {link['title']}: {link['link']}\n"
        
        return formatted.strip() or "No results found."