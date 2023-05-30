---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - apps
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.apps.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `appManifest` | `object` |
| `appDefinition` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getApp` | `SELECT` | `uuid, region` | Gets the app with the given universally unique identifier (UUID). |
| `listApps` | `SELECT` | `region` | Lists all available apps from the App Catalog. |
