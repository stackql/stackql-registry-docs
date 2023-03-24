---
title: upgrades
hide_title: false
hide_table_of_contents: false
keywords:
  - upgrades
  - kubernetes
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>upgrades</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.kubernetes.upgrades</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `supported_features` | `array` | The features available with the version of Kubernetes provided by a given slug. |
| `kubernetes_version` | `string` | The upstream version string for the version of Kubernetes provided by a given slug. |
| `slug` | `string` | The slug identifier for an available version of Kubernetes for use when creating or updating a cluster. The string contains both the upstream version of Kubernetes as well as the DigitalOcean revision. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_availableUpgrades` | `SELECT` | `cluster_id` |
| `_get_availableUpgrades` | `EXEC` | `cluster_id` |
