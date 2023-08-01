---
title: policies_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies_policies
  - iam
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
<tr><td><b>Name</b></td><td><code>policies_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.policies_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `policies` | `array` | Metadata for the policies that are attached to the resource. |
| `nextPageToken` | `string` | A page token that you can use in a ListPoliciesRequest to retrieve the next page. If this field is omitted, there are no additional pages. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_policies` | `SELECT` | `policiesId, policiesId1` |
