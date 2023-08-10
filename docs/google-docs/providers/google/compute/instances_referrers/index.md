---
title: instances_referrers
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_referrers
  - compute
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
<tr><td><b>Name</b></td><td><code>instances_referrers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instances_referrers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `target` | `string` | URL of the resource to which this reference points. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#reference for references. |
| `referenceType` | `string` | A description of the reference type with no implied semantics. Possible values include: 1. MEMBER_OF  |
| `referrer` | `string` | URL of the resource which refers to the target. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_referrers` | `SELECT` | `instance, project, zone` |
