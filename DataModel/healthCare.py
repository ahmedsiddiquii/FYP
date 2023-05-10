# note :
# 0 = label,  1 = text field, 2 = cehck box

data = {
  "Domain": {
    "hospitalManagement": {
      "person_party": {
        "person_detail": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 2,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "last_name": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Last Name",
            "type": 1,
          },
          "first_name": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "first Name",
            "type": 1,
          },
          "middle_name": {
              "data_type":"varchar(255)",
              "checkable":True,
               "label": "middle Name",
              "type": 1,
          },
          "personal_title": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Personal title",
            "type": 1,
          },
          "suffix": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "suffix",
            "type": 1,
          },
          "nickname": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "nickname",
            "type": 1,
          },
          "gender": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Gender",
            "type": 1,
          },
          "birthdate": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Birth Date",
            "type": 1,
          },
          "height": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Height",
            "type": 1,
          },
          "weight": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Weight",
            "type": 1,
          },
          "mother_maiden_name": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Mother maiden Name",
            "type": 1,
          },
          "maritial_status": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Martial status",
            "type": 1,
          },
          "social_security_no": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Social Security No",
            "type": 1,
          },
          "passport_no": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Passport No",
            "type": 1,
          },
          "passport_expire_date": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Passport Expire Date",
            "type": 1,
          },
          "total_year_work_experience": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Total year work experience",
            "type": 1,
          },
          "comment": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "comment",
            "type": 1,
          },
          "country": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "country",
            "type": 1,
          },
          "citizenship": {
            "data_type":"varchar(255)",
            "checkable":True,
            "label": "Citizenship",
            "type": 1,
          },
            },
        "person_role": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 2,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "indivitual_health_care": {
            "data_type": "bool",
            "checkable": True,
            "label": "Individual Health Care",
            "type": 2,
          },
          "employee": {
            "data_type": "bool",
            "checkable": True,
            "label": "Employee",
            "type": 2,
          },
          "contract": {
            "data_type": "bool",
            "checkable": True,
            "label": "contact",
            "type": 2,
          },
          "patient": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Patient",
            "type": 2,
          },

        },
        "insured_party": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 2,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "insured_indivitual": {
            "data_type": "bool",
            "checkable": True,
            "label": "Insured Individual",
            "type": 2,
          },
          "insured_organization": {
            "data_type": "bool",
            "checkable": True,
            "label": "Insured Organization",
            "type":2,
          }
        },
        "organization_role": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 2,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "Health Care Provider Organization": {
            "data_type": "datetime",
            "checkable": False,
            "label": "Health Care Provider Organization",
            "type": 2,
          },
          "Organization Unit": {
            "data_type": "datetime",
            "checkable": False,
            "label": "Organization Unit",
            "type": 2,
          },
          "Internal Organization": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Internal Organization",
            "type": 2,
          },
          "groupp": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Group",
            "type": 2,
          },
          "Employer": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Employer",
            "type": 2,
          },
          "Network": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Network",
            "type": 2,
          },
          "Supplier": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Supplier",
            "type": 2,
          },
          "Third Party": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Third Party",
            "type": 2,
          },
          "Insurance Provider": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Insurance Provider",
            "type": 2,
          },
          "Payor": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Payor",
            "type": 2,
          },
          "InternalOrganization1": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Internal Organization",
            "type": 2,
          }
        }
      },
      "orders": {
        "order_details": {
          "id": {
            "data_type": "int",
            "checkable":False,
            "label": "ID",
            "type": 2,
            "constraint": "NOT NULL AUTO_INCREMET"
          },
          "item_id": {
            "data_type": "int",
            "checkable": False,
            "label": "Item ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMET"
          },
          "quantity": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "Quantity",
            "type": 1,
          },
          "price": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "Price",
            "type": 1,
          },
          "order_date": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "Order Date",
            "type": 1,
          },
          "order_type": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "Order Type",
            "type": 1,
          },
          "product": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "Product",
            "type": 1,
          },
        },
        "agreement_item": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 2,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "item_seq_id": {
            "data_type": "int",
            "checkable": False,
            "label": "Item Sequence ID",
            "type": 1,
          },
          "text": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Text",
            "type": 1,
          },
          "image": {
            "data_type": "blob",
            "checkable": False,
            "label": "Image",
            "type": 1,
          },
          "pricing_program": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Pricing Program",
            "type": 2,
          },
          "sub_agreement": {
            "data_type": "bool",
            "checkable": True,
            "label": "Sub Agreement",
            "type": 2,
          },
          "agreement_exhibit": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Agreement exhibit",
            "type": 2,
          },
          "main_agreement": {
            "data_type": "boolean",
            "checkable": True,
            "label": "Main Agreement",
            "type": 2,
          },
          "agreement_section": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Agreement section",
            "type": 1,
          }
        },
        "agreement": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 2,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "patient_provider_agreement": {
            "data_type": "int",
            "checkable": False,
            "label": "Patient Provider Agreement",
            "type": 2,
          },
          "date": {
            "data_type": "datetime",
            "checkable": False,
            "label": "Date",
            "type": 1,
          },
          "from_date": {
            "data_type": "datetime",
            "checkable": False,
            "label": "From Date",
            "type": 1,
          },
          "thru_date": {
            "data_type": "datetime",
            "checkable": False,
            "label": "Thru Date",
            "type": 1,
          },
          "description": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "description",
            "type": 1,
          },
          "employee_agreement": {
            "data_type": "bool",
            "checkable": True,
            "label": "Employee Agreement",
            "type": 2,
          },
          "purchase_agreement": {
            "data_type": "boolean",
            "checkable": True,
            "label": "Purchase Agreement",
            "type": 2,
          },
          "provider_network_agreement": {
            "data_type": "bool",
            "checkable": True,
            "label": "Provider Network Agreement",
            "type": 2,
          },
          "other_agreement": {
            "data_type": "bool",
            "checkable": True,
            "label": "Other Agreement",
            "type": 1,
          },
          "insuarance_policy": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Insurance Policy",
            "type": 1,
          }
        },
        "agreement_role": {

        },
        "agreement_role_type": {

        },
        "agreement_type": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "type_id": {
            "data_type": "int",
            "checkable": True,
            "label": "Type ID",
            "type": 1,
          },
          "description": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Description",
            "type": 1,
          }
        },
        "party_relations": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "from_date": {
            "data_type": "datetime",
            "checkable": False,
            "label": "From Date",
            "type": 1,
          },
          "thru_date": {
            "data_type": "datetime",
            "checkable": False,
            "label": "Thru Date",
            "type": 1,
          },
          "comments": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Comment",
            "type": 1,
          }
        },
        "party_role": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "role_id": {
            "data_type": "datetime",
            "checkable": False,
            "label": "Role ID",
            "type": 1,
          }
        },
        "party": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "party_id": {
            "data_type": "datetime",
            "checkable": False,
            "label": "Party ID",
            "type": 1,
          },
          "person": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Person",
            "type": 1,
          },
          "organization": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Organization",
            "type": 1,
          }
        }
      },
      "products": {
        "product_details": {
          "id": {
            "data_type": "int",
            "checkable":False,
            "constraint": "NOT NULL AUTO_INCREMET"
          },
          "name": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "name",
            "type": 1,
          },
          "intro_date": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "intro date",
            "type": 1,
          },
          "sale_discontinuation_date": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "sale discontinious date",
            "type": 1,
          },
          "support_discontinuation_date": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "support discontinious date",
            "type": 1,
          },
          "comment": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "comment",
            "type": 1,
          },
          "health": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "health",
            "type": 1,
          },
          "category": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "category",
            "type": 1,
          },
          "color": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "color",
            "type": 1,
          },
          "quality": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "quality",
            "type": 1,
          },
          "brand_name": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "brand name",
            "type": 1,
          },
          "rating": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "rating",
            "type": 1,
          },
          "supplier": {
            "data_type": "varchar(255)",
            "checkable":True,
            "label": "supplier",
            "type": 1,
          },
        },
        "category": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "category_id": {
            "data_type": "int",
            "checkable": False,
            "label": "Category ID",
            "type": 1,
          },
          "discription": {
            "data_type": "int",
            "checkable": False,
            "label": "Description",
            "type": 2,
          },
          "hospital_category": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "hospital Category",
            "type": 2,
          },
          "dental_category": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Dental Category",
            "type": 2,
          },
          "physician_ category": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Physician Category",
            "type": 2,
          },
          "vision_category": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Vision Category",
            "type": 2,
          },
          "alternative_med_category": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Alternative Med Category",
            "type": 2,
          },
          "other_healthcare_category": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Other Healthcare Category",
            "type": 2,
          },
          "agreement_section": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Agreement Section",
            "type": 2,
          }
        },
        "category_offering": {

        },
        "health_care_offering": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "health_care_offering_id": {
            "data_type": "int",
            "checkable": False,
            "label": "HealthCare Offering ID",
            "type": 1,
          },
          "name": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Name",
            "type": 1,
          },
          "from_date": {
            "data_type": "datetime",
            "checkable": False,
            "label": "From Date",
            "type": 1,
          },
          "thru_date": {
            "data_type": "datetime",
            "checkable": False,
            "label": "Thru Date",
            "type": 1,
          },
          "description": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "Description",
            "type": 1,
          },
          "employee_agreement": {
            "data_type": "bool",
            "checkable": True,
            "label": "Employee Agreement",
            "type": 2,
          },
          "purchase_agreement": {
            "data_type": "boolean",
            "checkable": True,
            "label": "Purchase Agreement",
            "type": 2,
          },
          "provider_network_agreement": {
            "data_type": "bool",
            "checkable": True,
            "label": "Provider Network Agreement",
            "type": 2,
          },
          "other_agreement": {
            "data_type": "bool",
            "checkable": True,
            "label": "Other Agreement",
            "type": 2,
          },
          "insuarance_policy": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Insurance Policy",
            "type": 2,
          }
        },
        "health_care_service_offering": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "procedure_id": {
            "data_type": "int",
            "checkable": True,
            "label": "Procedure ID",
            "type": 1,
          },
          "other_healt_care_offering": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Other Health Care Offering",
            "type": 2,
          }
        },
        "health_care_good_offering": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "procedure_id": {
            "data_type": "int",
            "checkable": True,
            "label": "Procedure ID",
            "type": 1,
          },
          "other_healt_care_offering": {
            "data_type": "varchar(255)",
            "checkable": True,
            "label": "Other Health Care Offering",
            "type": 2,
          }
        },
        "inventory_item": {

        },
        "provider_offering": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "label": "ID",
            "type": 1,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "from_date": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "From Date",
            "type": 1,
          },
          "thu_date": {
            "data_type": "varchar(255)",
            "checkable": False,
            "label": "thru Date",
            "type": 1,
          }
        },
        "health_care_provider_organization": {

        }
      },
      "shipment_delivery": {
          "shipment_details": {
            "id": {
              "data_type":"int",
              "checkable": False,
              "label": "ID",
              "type": 1,
              "constraint":"NOT NULL AUTO_INCREMENT"
          },
            "quantity":{
                "data_type":"varchar(255)",
                "checkable":True,
                "label": "ID",
                "type": 1,
          },
            "inventory_item":{
          "data_type":"varchar(255)",
          "checkable":True,
          "label": "Inventory Item",
          "type": 1,
          },
            "status":{
              "data_type":"varchar(255)",
              "checkable":True,
              "label": "status",
              "type": 1,
          },
            "status_date":{
          "data_type":"varchar(255)",
          "checkable":True,
          "label": "status Date",
          "type": 1,
          },
            "order_id":{
          "data_type":"int",
          "checkable":False,
          "label": "Order ID",
          "type": 1,
          "constraint":"NOT NULL AUTO_INCREMET"
          },
            },
          "healthcare_delivery": {
              "id": {
                  "data_type": "int",
                  "checkable": False,
                  "label": "ID",
                  "type": 1,
                  "constraint": "NOT NULL AUTO_INCREMENT"
              },
              "from_date": {
                  "data_type": "date",
                  "checkable": True,
                "label": "From Date",
                "type": 1,
              },
              "thru_date": {
                  "data_type": "date",
                  "checkable": True,
                  "label": "Thru Date",
                  "type": 1,
              },
              "notes": {
                  "data_type": "varchar(255)",
                  "checkable": True,
                  "label": "Notes",
                  "type": 1,
              }
          },
          "symptoms": {
              "id": {
                  "data_type": "int",
                  "checkable": False,
                  "label": "ID",
                  "type": 1,
                  "constraint": "NOT NULL AUTO_INCREMENT"
              },
              "description_id": {
                  "data_type": "int",
                  "checkable": True,
                  "label": "Description ID",
                  "type": 1,
              }
          },
          "symptom_type": {
                  "id": {
                      "data_type": "int",
                      "checkable": False,
                      "label": "ID",
                      "type": 1,
                      "constraint": "NOT NULL AUTO_INCREMENT"
                  },
                  "description": {
                      "data_type": "varchar(255)",
                      "checkable": True,
                      "label": "Description",
                      "type": 1,
                  }
              },
          "healthcare_episode": {
              "id": {
                  "data_type": "int",
                  "checkable": False,
                  "label": "ID",
                  "type": 1,
                  "constraint": "NOT NULL AUTO_INCREMENT"
              },
              "episode_create_date": {
                  "data_type": "date",
                  "checkable": True,
                  "label": "Episode Create Date",
                  "type": 1,
              },
              "description": {
                  "data_type": "varchar(255)",
                  "checkable": True,
                  "label": "Description",
                  "type": 1,
              }
          },
          "incident": {
              "id": {
                  "data_type": "int",
                  "checkable": False,
                  "label": "ID",
                  "type": 1,
                  "constraint": "NOT NULL AUTO_INCREMENT"
              },
              "date": {
                  "data_type": "date",
                  "checkable": True,
                  "label": "Date",
                  "type": 1,
              },
              "description": {
                  "data_type": "varchar(255)",
                  "checkable": True,
                  "label": "ID",
                  "type": 1,
              },
              "mpl_related_ind": {
                  "data_type": "bool",
                  "checkable": True,
                  "label": "MPL Related Ind",
                  "type": 1,
              },
          },
          "incident_type": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "label": "ID",
                "type": 1,
                "constraint":"NOT NULL AUTO_INCREMENT"
              },
              "description": {
                "data_type":"varchar(255)",
                "checkable":True,
                "label": "Description",
                "type": 1,
              },
                },
          "visit_reason": {
            "id": {
                "data_type": "int",
                "checkable": False,
                "constraint": "NOT NULL AUTO_INCREMENT",
              },
            "description": {
              "data_type": "varchar(255)",
              "checkable": True,
              "label": "description",
              "type": 1,
            },
          },
          "health_care_visit": {
            "id":{
                "data_type":"int",
                "checkable":False,
                "label": "ID",
                "type": 1,
                "constraint":"NOT NULL AUTO_INCREMENT"
                },
            "from_date": {
                "data_type":"date",
                "checkable":True,
                "label": "From Date",
                "type": 1,
            },
            "thru_date": {
              "data_type":"date",
              "checkable":True,
              "label": "thru Date",
              "type": 1,
                },
          },
          "patient": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "label": "patient id",
                "type": 1,
                "constraint":"NOT NULL AUTO_INCREMET"
              },
          },
          "episode_type": {
              "id": {
                "data_type": "int",
                "checkable": False,
                "label": "episode ID",
                "type": 1,
                "constraint": "NOT NULL AUTO_INCREMET"
              },
          },
          "health_care_visit_role": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",
                "label": "health care visit role id",
                "type": 1,
              },
          },
          "health_care_visit_role_type": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",
                "label": "health care role visit type",
                "type": 1,
              },
          },
          "party": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",
                "label": "party id",
                "type": 1,
              },
          },
          "health_care_visit_status": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",
                "label": "party id",
                "type": 1,
              },
              "status_datetime": {
                "data_type": "DATETIME",
                "checkable": False,
                "label": "health care visit status",
                "type": 1,
              },
          },
          "health_care_visit_status_type": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",
                "label": "health visit status type",
                "type": 1,
              },
          },
          "postal_address": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET"
              },
              "address_1": {
                "data_type": "varchar(255)",
                "checkable": True,
                "label": "address 1",
                "type": 1,
              },
              "address_2": {
                "data_type": "varchar(255)",
                "checkable": True,
                "label": "address 2",
                "type": 1,
              },
              "directions": {
                "data_type": "varchar(255)",
                "checkable": True,
                "label": "direction",
                "type": 1,
              },
          },
          "facility": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET"
              },
              "description": {
                "data_type":"varchar(255)",
                "checkable":True,
                "label": "discription",
                "type": 1,
              },
          },
          "hospital": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",
                "label": "hospital id",
                "type": 1,
              },
          },
          "medical_office": {
              "id": {
                "data_type": "int",
                "checkable": False,
                "constraint": "NOT NULL AUTO_INCREMET",
                "label": "medical office id",
                "type": 1,
              },
          },
          "clinic": {
              "id":{
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",
                "label": "clinic id",
                "type": 1,
              },
          },
          "ambulatory_surgery_center": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",
                "label": "ambulatory surgery center id",
                "type": 1,
              },
          },
          "other_healthcare_facility": {
              "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",
                "label": "other healthcare facility",
                "type": 1,
              },
                },
      },
      "healthcare_claims": {
        "invoice_details": {
            "id": {
            "data_type":"int",
            "checkable":False,
            "constraint":"NOT NULL AUTO_INCREMET"
            },
            "invoice_date": {
              "data_type":"varchar(255)",
              "checkable":True,
              "label": "invoice date",
              "type": 1,
            },
            "message": {
              "data_type":"varchar(255)",
              "checkable":True,
              "label": "message",
              "type": 1,
            },
            "description": {
              "data_type":"varchar(255)",
              "checkable":True,
              "label": "description",
              "type": 1,
            },
            "product": {
              "data_type": "varchar(255)",
              "checkable": True,
              "label": "product",
              "type": 1,
            },
            "quantity": {
              "data_type":"varchar(255)",
              "checkable":True,
              "label": "quantity",
              "type": 1,
            },
            "price": {
              "data_type":"varchar(255)",
              "checkable":True,
              "label": "price",
              "type": 1,
            },
            "tax": {
              "data_type":"varchar(255)",
              "checkable":True,
              "label": "tax",
              "type": 1,
            },
            "address": {
              "data_type":"varchar(255)",
              "checkable":True,
              "label": "address",
              "type": 1,
            },
              },
        "healthcare_delivery_claim_submission": {
          "id": {
                "data_type":"int",
                "checkable":False,
                "constraint":"NOT NULL AUTO_INCREMET",

              },
          "claim_submission": {
              "data_type": "bool",
              "checkable": False,
              "label": "claim submissin",
              "type": 1,

            }
        },
        "claim_settlement": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "date_settled": {
            "data_type": "bool",
            "checkable": False,
            "label": "date settled",
            "type": 1,


          }

        },
        "claim_settlement_amount": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "Amount": {
            "data_type": "bool",
            "checkable": False,
            "label": "Amount",
            "type": 1,


          }
        },
        "claim_item": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "amount": {
            "data_type": "bool",
            "checkable": False,
            "label": "amount",
            "type": 1,


          },
          "quantity": {
            "data_type": "bool",
            "checkable": False,
            "label": "quantity",
            "type": 1,
          }
        },
        "payment": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "effective_date": {
            "data_type": "bool",
            "checkable": False,
            "label": "effective date",
            "type": 1,
          },
          "payment_ref_num": {
            "data_type": "bool",
            "checkable": False,
            "label": "payment reference num",
            "type": 1,
          },
          "amount": {
            "data_type": "bool",
            "checkable": False,
            "label": "amount",
            "type": 1,
          },
          "comment": {
            "data_type": "bool",
            "checkable": False,
            "label": "comment",
            "type": 1,
          }
        },
        "healthcare_delivery": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "delivery_notes": {
            "data_type": "bool",
            "checkable": False,
            "label": "delivery notes",
            "type": 1,
          },
        },
        "unit_of_measure": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "abbreviation": {
            "data_type": "bool",
            "checkable": False,
            "label": "abbreviation",
            "type": 1,
          },
          "description": {
            "data_type": "bool",
            "checkable": False,
            "label": "description",
            "type": 1,
          },
        },
        "claim": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "submission_date": {
            "data_type": "DATETIME",
            "checkable": False,
            "label": "submission date",
            "type": 1,


          },
          "claim_type": {
            "data_type": "varchar",
            "checkable": True,
            "label": "claim date",
            "type": 1,
          },
        },
        "claim_status": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "date_time": {
            "data_type": "DATETIME",
            "checkable": False,
            "label": "date ",
            "type": 1,
          },
        },
        "claim_status_type": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
        },
      },
    }
  }
}