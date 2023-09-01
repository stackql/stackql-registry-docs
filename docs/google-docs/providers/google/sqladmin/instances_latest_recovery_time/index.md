---
title: instances_latest_recovery_time
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_latest_recovery_time
  - sqladmin
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
<tr><td><b>Name</b></td><td><code>instances_latest_recovery_time</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sqladmin.instances_latest_recovery_time</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | This is always `sql#getLatestRecoveryTime`. |
| `latestRecoveryTime` | `string` | Timestamp, identifies the latest recovery time of the source instance. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_latest_recovery_time` | `SELECT` | `instance, project` |
