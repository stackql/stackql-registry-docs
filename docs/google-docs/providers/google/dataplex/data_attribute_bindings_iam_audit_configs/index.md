---
title: data_attribute_bindings_iam_audit_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - data_attribute_bindings_iam_audit_configs
  - dataplex
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
<tr><td><b>Name</b></td><td><code>data_attribute_bindings_iam_audit_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.data_attribute_bindings_iam_audit_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `service` | `string` | Specifies a service that will be enabled for audit logging. For example, storage.googleapis.com, cloudsql.googleapis.com. allServices is a special value that covers all services. |
| `auditLogConfigs` | `array` | The configuration for logging of each type of permission. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_dataAttributeBindings_getIamPolicy` | `SELECT` | `dataAttributeBindingsId, locationsId, projectsId` |