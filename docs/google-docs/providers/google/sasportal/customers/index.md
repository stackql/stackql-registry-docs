---
title: customers
hide_title: false
hide_table_of_contents: false
keywords:
  - customers
  - sasportal
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sasportal.customers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the customer. |
| `displayName` | `string` | Required. Name of the organization that the customer entity represents. |
| `sasUserIds` | `array` | User IDs used by the devices belonging to this customer. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_get` | `SELECT` | `customersId` | Returns a requested customer. |
| `customers_list` | `SELECT` |  | Returns a list of requested customers. |
| `customers_check_has_provisioned_deployment` | `EXEC` |  | Checks whether a SAS deployment for the authentication context exists. |
| `customers_migrate_organization` | `EXEC` |  | Migrates a SAS organization to the cloud. This will create GCP projects for each deployment and associate them. The SAS Organization is linked to the gcp project that called the command. go/sas-legacy-customer-migration |
| `customers_patch` | `EXEC` | `customersId` | Updates an existing customer. |
| `customers_provision_deployment` | `EXEC` |  | Creates a new SAS deployment through the GCP workflow. Creates a SAS organization if an organization match is not found. |
