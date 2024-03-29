---
title: instances_shielded_instance_identity
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_shielded_instance_identity
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
<tr><td><b>Name</b></td><td><code>instances_shielded_instance_identity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.instances_shielded_instance_identity</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `encryptionKey` | `object` | A Shielded Instance Identity Entry. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#shieldedInstanceIdentity for shielded Instance identity entry. |
| `signingKey` | `object` | A Shielded Instance Identity Entry. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_shielded_instance_identity` | `SELECT` | `instance, project, zone` |
