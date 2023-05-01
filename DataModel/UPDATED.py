data = {
  "Domain": {
    "hospitalManagement": {
      "person_party": {
        "person_role": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
          "groupp": {
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "role_id": {
            "data_type": "datetime",
            "checkable": False
          }
        },
        "party": {
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
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
          "id": {
            "data_type": "int",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"
          },
          "from_date": {
            "data_type": "varchar(255)",
            "checkable": False
          },
          "thu_date": {
            "data_type": "varchar(255)",
            "checkable": False
          }
        },
        "health_care_provider_organization": {

        }
      },
      "shipment_delivery": {
          "healthcare_delivery": {
              "id": {
                  "data_type": "int",
                  "checkable": False,
                  "constraint": "NOT NULL AUTO_INCREMENT"
              },
              "from_date": {
                  "data_type": "date",
                  "checkable": True
              },
              "thru_date": {
                  "data_type": "date",
                  "checkable": True
              },
              "notes": {
                  "data_type": "varchar(255)",
                  "checkable": True
              }
          },
          "symptoms": {
              "id": {
                  "data_type": "int",
                  "checkable": False,
                  "constraint": "NOT NULL AUTO_INCREMENT"
              },
              "description_id": {
                  "data_type": "int",
                  "checkable": True
              }

          },
          "symptom_type": {
                  "id": {
                      "data_type": "int",
                      "checkable": False,
                      "constraint": "NOT NULL AUTO_INCREMENT"
                  },
                  "description": {
                      "data_type": "varchar(255)",
                      "checkable": True
                  }
              },
          "healthcare_episode": {
              "id": {
                  "data_type": "int",
                  "checkable": False,
                  "constraint": "NOT NULL AUTO_INCREMENT"
              },
              "episode_create_date": {
                  "data_type": "date",
                  "checkable": True
              },
              "description": {
                  "data_type": "varchar(255)",
                  "checkable": True
              }
          },
          "incident": {
              "id": {
                  "data_type": "int",
                  "checkable": False,
                  "constraint": "NOT NULL AUTO_INCREMENT"
              },
              "date": {
                  "data_type": "date",
                  "checkable": True
              },
              "description": {
                  "data_type": "varchar(255)",
                  "checkable": True
              },
              "mpl_related_ind": {
                  "data_type": "bool",
                  "checkable": True
              },

  },
          "incident_type":{
	"id":{
	"data_type":"int",
	"checkable":False,
	"constraint":"NOT NULL AUTO_INCREMENT"
	},
	"description":{
	"data_type":"varchar(255)",
	"checkable":True
	},
      },
        "visit_reason":{
	"id":{
	"data_type":"int",
	"checkable":False,
	"constraint":"NOT NULL AUTO_INCREMENT"
	},
	"description":{
	"data_type":"varchar(255)",
	"checkable":True
	},
      },

"health_care_visit":{
"id":{
	"data_type":"int",
	"checkable":False,
	"constraint":"NOT NULL AUTO_INCREMENT"
	},
"from_date":{
	"data_type":"date",
	"checkable":True
},
	"thru_date":{
"data_type":"date",
	"checkable":True
	},


      },
      },
      "healthcare_claims":{
        "healthcare_delivery_claim_submission":{
        "claim_submission":{
            "data_type":"bool",
            "checkable": False,

          }
        },
        "claim_settlement": {
          "id": {
            "data_type": "bool",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "date_settled": {
            "data_type": "bool",
            "checkable": False,


          }

        },
        "claim_settlement_amount": {
          "id": {
            "data_type": "bool",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "Amount": {
            "data_type": "bool",
            "checkable": False,


          }

    },
        "claim_item": {
          "id": {
            "data_type": "bool",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "amount": {
            "data_type": "bool",
            "checkable": False,


          },
          "quantity": {
            "data_type": "bool",
            "checkable": False,


          }

    },
        "payment": {
          "id": {
            "data_type": "bool",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "effective_date": {
            "data_type": "bool",
            "checkable": False,


          },
          "payment_ref_num": {
            "data_type": "bool",
            "checkable": False,


          },
          "amount": {
            "data_type": "bool",
            "checkable": False,


          },
          "comment": {
            "data_type": "bool",
            "checkable": False,


          }

    },
        "healthcare_delivery": {
          "id": {
            "data_type": "bool",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "delivery_notes": {
            "data_type": "bool",
            "checkable": False,


          },

    },
        "unit_of_measure": {
          "id": {
            "data_type": "bool",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "abbreviation": {
            "data_type": "bool",
            "checkable": False,


          },
          "description": {
            "data_type": "bool",
            "checkable": False,


          },

    },
        "claim": {
          "id": {
            "data_type": "bool",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "submission_date": {
            "data_type": "date_time",
            "checkable": False,


          },
          "claim_type": {
            "data_type": "varchar",
            "checkable": True,


          },


    },
        "claim_status": {
          "id": {
            "data_type": "bool",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },
          "date_time": {
            "data_type": "date_time",
            "checkable": False,


          },



    },
        "claim_status_type": {
          "id": {
            "data_type": "bool",
            "checkable": False,
            "constraint": "NOT NULL AUTO_INCREMENT"

          },



    },

},


}
}
}