---
title: trusted_access_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - trusted_access_roles
  - container_service
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trusted_access_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_service.trusted_access_roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of role, name is unique under a source resource type |
| `rules` | `array` | List of rules for the role. This maps to 'rules' property of [Kubernetes Cluster Role](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/#ClusterRole). |
| `sourceResourceType` | `string` | Resource type of Azure resource |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `TrustedAccessRoles_List` | `SELECT` | `location, subscriptionId` |
