---
title: vpcs
hide_title: false
hide_table_of_contents: false
keywords:
  - vpcs
  - vpcs
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
<tr><td><b>Name</b></td><td><code>vpcs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.vpcs.vpcs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique ID that can be used to identify and reference the VPC. |
| `name` | `string` | The name of the VPC. Must be unique and may only contain alphanumeric characters, dashes, and periods. |
| `description` | `string` | A free-form text field for describing the VPC's purpose. It may be a maximum of 255 characters. |
| `urn` | `string` | The uniform resource name (URN) for the resource in the format do:resource_type:resource_id. |
| `ip_range` | `string` | The range of IP addresses in the VPC in CIDR notation. Network ranges cannot overlap with other networks in the same account and must be in range of private addresses as defined in RFC1918. It may not be smaller than `/28` nor larger than `/16`. If no IP range is specified, a `/20` network range is generated that won't conflict with other VPC networks in your account. |
| `region` | `string` | The slug identifier for the region where the VPC will be created. |
| `default` | `boolean` | A boolean value indicating whether or not the VPC is the default network for the region. All applicable resources are placed into the default VPC network unless otherwise specified during their creation. The `default` field cannot be unset from `true`. If you want to set a new default VPC network, update the `default` field of another VPC network in the same region. The previous network's `default` field will be set to `false` when a new default VPC has been defined. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `vpc_id` | To show information about an existing VPC, send a GET request to `/v2/vpcs/$VPC_ID`. |
| `list` | `SELECT` |  | To list all of the VPCs on your account, send a GET request to `/v2/vpcs`. |
| `create` | `INSERT` | `data__name, data__region` | To create a VPC, send a POST request to `/v2/vpcs` specifying the attributes<br />in the table below in the JSON body.<br /><br />**Note:** If you do not currently have a VPC network in a specific datacenter<br />region, the first one that you create will be set as the default for that<br />region. The default VPC for a region cannot be changed or deleted.<br /> |
| `delete` | `DELETE` | `vpc_id` | To delete a VPC, send a DELETE request to `/v2/vpcs/$VPC_ID`. A 204 status<br />code with no body will be returned in response to a successful request.<br /><br />The default VPC for a region can not be deleted. Additionally, a VPC can only<br />be deleted if it does not contain any member resources. Attempting to delete<br />a region's default VPC or a VPC that still has members will result in a<br />403 Forbidden error response.<br /> |
| `_get` | `EXEC` | `vpc_id` | To show information about an existing VPC, send a GET request to `/v2/vpcs/$VPC_ID`. |
| `_list` | `EXEC` |  | To list all of the VPCs on your account, send a GET request to `/v2/vpcs`. |
| `patch` | `EXEC` | `vpc_id` | To update a subset of information about a VPC, send a PATCH request to<br />`/v2/vpcs/$VPC_ID`.<br /> |
| `update` | `EXEC` | `vpc_id, data__name` | To update information about a VPC, send a PUT request to `/v2/vpcs/$VPC_ID`.<br /> |
