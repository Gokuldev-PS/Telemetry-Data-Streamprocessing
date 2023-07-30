variable "confluent_cloud_api_key" {
  description = "Confluent Cloud API Key (also referred as Cloud API ID)"
  type        = string
  default = "ZKPDQLF2POQEEAOT"
}

variable "confluent_cloud_api_secret" {
  description = "Confluent Cloud API Secret"
  type        = string
  sensitive   = true
  default = "7zUeI/Zuj6rfiw6vI1Zs474JRamT4ynnd7i498cA1m5pWTWsPBayG9SQvNjRLYLO"
}