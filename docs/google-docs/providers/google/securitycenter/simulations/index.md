---
title: simulations
hide_title: false
hide_table_of_contents: false
keywords:
  - simulations
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>simulations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.simulations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Full resource name of the Simulation: organizations/123/simulations/456 |
| `resourceValueConfigsMetadata` | `array` | Resource value configurations' metadata used in this simulation. Maximum of 100. |
| `createTime` | `string` | Output only. Time simulation was created |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_simulations_get` | `SELECT` | `organizationsId, simulationsId` |
