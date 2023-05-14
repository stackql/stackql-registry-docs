---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - lke
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.lke.versions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getLKEVersion` | `SELECT` | `version` | View a Kubernetes version available for deployment to a Kubernetes cluster.<br /> |
| `getLKEVersions` | `SELECT` |  | List the Kubernetes versions available for deployment to a Kubernetes cluster.<br /> |
| `_getLKEVersion` | `EXEC` | `version` | View a Kubernetes version available for deployment to a Kubernetes cluster.<br /> |
| `_getLKEVersions` | `EXEC` |  | List the Kubernetes versions available for deployment to a Kubernetes cluster.<br /> |
