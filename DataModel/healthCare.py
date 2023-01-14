data = {
  "Domain": {
    "hospitalManagement": {
      "person/party": {
        "person_role": {
          "person_role_id": {
            "data_type": "int",
            "checkable": False
          },
          "indivitual_health_care": {
            "data_type": "bool",
            "checkable": True
          },
          "employee": {
            "data_type": "bool",
            "checkable": True
          },
          "contact": {
            "data_type": "bool",
            "checkable": True
          },
          "patient": {
            "data_type": "varchar(255)",
            "checkable": True
          }
        },
        "insured_party": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "insured_indivitual": {
            "data_type": "bool",
            "checkable": True
          },
          "insured_organization": {
            "data_type": "bool",
            "checkable": True
          }
        },
        "organization_role": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "Health Care Provider Organization": {
            "data_type": "datetime",
            "checkable": False
          },
          "Organization Unit": {
            "data_type": "datetime",
            "checkable": False
          },
          "Internal Organization": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "group": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "Employer": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "Network": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "Supplier": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "Third Party": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "Insurance Provider": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "Payor": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "InternalOrganization1": {
            "data_type": "varchar(255)",
            "checkable": False
          }
        }
      },
      "orders": {
        "agreement_item": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "item_seq_id": {
            "data_type": "int",
            "checkable": False
          },
          "text": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "image": {
            "data_type": "blob",
            "checkable": False
          },
          "pricing_program": {
            "data_type": "varchar(255)",
            "checkable": True
          },
          "sub_agreement": {
            "data_type": "bool",
            "checkable": True
          },
          "agreement_exhibit": {
            "data_type": "varchar(255)",
            "checkable": True
          },
          "main_agreement": {
            "data_type": "boolean",
            "checkable": True
          },
          "agreement_section": {
            "data_type": "varchar(255)",
            "checkable": True
          }
        },
        "agreement": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "patient_provider_agreement": {
            "data_type": "int",
            "checkable": False
          },
          "date": {
            "data_type": "datetime",
            "checkable": False
          },
          "from_date": {
            "data_type": "datetime",
            "checkable": False
          },
          "thru_date": {
            "data_type": "datetime",
            "checkable": False
          },
          "description": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "employee_agreement": {
            "data_type": "bool",
            "checkable": True
          },
          "purchase_agreement": {
            "data_type": "boolean",
            "checkable": True
          },
          "provider_network_agreement": {
            "data_type": "bool",
            "checkable": True
          },
          "other_agreement": {
            "data_type": "bool",
            "checkable": True
          },
          "insuarance_policy": {
            "data_type": "varchar(255)",
            "checkable": True
          }
        },
        "agreement_role": {

        },
        "agreement_role_type": {

        },
        "agreement_type": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "type_id": {
            "data_type": "int",
            "checkable": True
          },
          "description": {
            "data_type": "varchar(255)",
            "checkable": True
          }
        },
        "party_relations": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "from_date": {
            "data_type": "datetime",
            "checkable": False
          },
          "thru_date": {
            "data_type": "datetime",
            "checkable": False
          },
          "comments": {
            "data_type": "varchar(255)",
            "checkable": False
          }
        },
        "party_role": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "role_id": {
            "data_type": "datetime",
            "checkable": False
          }
        },
        "party": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "party_id": {
            "data_type": "datetime",
            "checkable": False
          },
          "person": {
            "data_type": "varchar(255)",
            "checkable": True
          },
          "organization": {
            "data_type": "varchar(255)",
            "checkable": True
          }
        }
      },
      "products": {
        "category": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "category_id": {
            "data_type": "int",
            "checkable": False
          },
          "discription": {
            "data_type": "int",
            "checkable": False
          },
          "hospital_category": {
            "data_type": "varchar(255)",
            "checkable": True
          },
          "dental_category": {
            "data_type": "varchar(255)",
            "checkable": True
          },
          "physician_ category": {
            "data_type": "varchar(255)",
            "checkable": True
          },
          "vision_category": {
            "data_type": "varchar(255)",
            "checkable": True
          },
          "alternative_med_category": {
            "data_type": "varchar(255)",
            "checkable": True
          },
          "other_healthcare_category": {
            "data_type": "varchar(255)",
            "checkable": True
          },
          "agreement_section": {
            "data_type": "varchar(255)",
            "checkable": True
          }
        },
        "category_offering": {

        },
        "health_care_offering": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "health_care_offering_id": {
            "data_type": "int",
            "checkable": False
          },
          "name": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "from_date": {
            "data_type": "datetime",
            "checkable": False
          },
          "thru_date": {
            "data_type": "datetime",
            "checkable": False
          },
          "description": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "employee_agreement": {
            "data_type": "bool",
            "checkable": True
          },
          "purchase_agreement": {
            "data_type": "boolean",
            "checkable": True
          },
          "provider_network_agreement": {
            "data_type": "bool",
            "checkable": True
          },
          "other_agreement": {
            "data_type": "bool",
            "checkable": True
          },
          "insuarance_policy": {
            "data_type": "varchar(255)",
            "checkable": True
          }
        },
        "health_care_service_offering": {
          "id": {
            "data_type": "int",
            "checkable": False
          },
          "procedure_id": {
            "data_type": "int",
            "checkable": True
          },
          "other_healt_care_offering": {
            "data_type": "varchar(255)",
            "checkable": True
          }
        },
        "health_care_good_offering": {
          "health_care_good_offering_id": {
            "data_type": "int",
            "checkable": False
          },
          "procedure_id": {
            "data_type": "int",
            "checkable": True
          },
          "other_healt_care_offering": {
            "data_type": "varchar(255)",
            "checkable": True
          }
        },
        "inventory_item": {

        },
        "provider_offering": {
          "provider_offering_id": {
            "data_type": "int",
            "checkable": False
          },
          "from_date": {
            "data_type": "\"varchar(255)\"",
            "checkable": False
          },
          "thu_date": {
            "data_type": "\"varchar(255)\"",
            "checkable": False
          }
        },
        "health_care_provider_organization": {

        }
      }
    }
  }
}