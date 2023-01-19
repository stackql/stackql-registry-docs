---
title: contact_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_groups
  - people
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.people.contact_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The contact group name set by the group owner or a system provided name for system groups. For [`contactGroups.create`](/people/api/rest/v1/contactGroups/create) or [`contactGroups.update`](/people/api/rest/v1/contactGroups/update) the name must be unique to the users contact groups. Attempting to create a group with a duplicate name will return a HTTP 409 error. |
| `resourceName` | `string` | The resource name for the contact group, assigned by the server. An ASCII string, in the form of `contactGroups/&#123;contact_group_id&#125;`. |
| `groupType` | `string` | Output only. The contact group type. |
| `memberCount` | `integer` | Output only. The total number of contacts in the group irrespective of max members in specified in the request. |
| `formattedName` | `string` | Output only. The name translated and formatted in the viewer's account locale or the `Accept-Language` HTTP header locale for system groups names. Group names set by the owner are the same as name. |
| `memberResourceNames` | `array` | Output only. The list of contact person resource names that are members of the contact group. The field is only populated for GET requests and will only return as many members as `maxMembers` in the get request. |
| `metadata` | `object` | The metadata about a contact group. |
| `etag` | `string` | The [HTTP entity tag](https://en.wikipedia.org/wiki/HTTP_ETag) of the resource. Used for web cache validation. |
| `clientData` | `array` | The group's client data. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `contactGroups_get` | `SELECT` | `contactGroupsId` | Get a specific contact group owned by the authenticated user by specifying a contact group resource name. |
| `contactGroups_list` | `SELECT` |  | List all contact groups owned by the authenticated user. Members of the contact groups are not populated. |
| `contactGroups_create` | `INSERT` |  | Create a new contact group owned by the authenticated user. Created contact group names must be unique to the users contact groups. Attempting to create a group with a duplicate name will return a HTTP 409 error. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures. |
| `contactGroups_delete` | `DELETE` | `contactGroupsId` | Delete an existing contact group owned by the authenticated user by specifying a contact group resource name. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures. |
| `contactGroups_batchGet` | `EXEC` |  | Get a list of contact groups owned by the authenticated user by specifying a list of contact group resource names. |
| `contactGroups_update` | `EXEC` | `contactGroupsId` | Update the name of an existing contact group owned by the authenticated user. Updated contact group names must be unique to the users contact groups. Attempting to create a group with a duplicate name will return a HTTP 409 error. Mutate requests for the same user should be sent sequentially to avoid increased latency and failures. |
