---
title: namespaces_iam_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_iam_policies
  - servicedirectory
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
<tr><td><b>Name</b></td><td><code>namespaces_iam_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.servicedirectory.namespaces_iam_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_iam_policy` | `EXEC` | `locationsId, namespacesId, projectsId` | Gets the IAM Policy for a resource (namespace or service only). |
| `set_iam_policy` | `EXEC` | `locationsId, namespacesId, projectsId` | Sets the IAM Policy for a resource (namespace or service only). |
| `test_iam_permissions` | `EXEC` | `locationsId, namespacesId, projectsId` | Tests IAM permissions for a resource (namespace or service only). |
