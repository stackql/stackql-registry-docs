---
title: scim_enterprise_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scim_enterprise_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.scim_enterprise_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `meta` | `object` |
| `schemas` | `array` |
| `displayName` | `string` |
| `externalId` | `string` |
| `members` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_provisioning_information_for_enterprise_group` | `SELECT` | `enterprise, scim_group_id` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change. |
| `list_provisioned_groups_enterprise` | `SELECT` | `enterprise` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change. |
| `provision_and_invite_enterprise_group` | `INSERT` | `enterprise, data__displayName, data__schemas` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change.<br /><br />Provision an enterprise group, and invite users to the group. This sends invitation emails to the email address of the invited users to join the GitHub organization that the SCIM group corresponds to. |
| `delete_scim_group_from_enterprise` | `DELETE` | `enterprise, scim_group_id` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change. |
| `set_information_for_provisioned_enterprise_group` | `EXEC` | `enterprise, scim_group_id, data__displayName, data__schemas` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change.<br /><br />Replaces an existing provisioned group’s information. You must provide all the information required for the group as if you were provisioning it for the first time. Any existing group information that you don't provide will be removed, including group membership. If you want to only update a specific attribute, use the [Update an attribute for a SCIM enterprise group](#update-an-attribute-for-a-scim-enterprise-group) endpoint instead. |
| `update_attribute_for_enterprise_group` | `EXEC` | `enterprise, scim_group_id, data__Operations, data__schemas` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change.<br /><br />Allows you to change a provisioned group’s individual attributes. To change a group’s values, you must provide a specific Operations JSON format that contains at least one of the add, remove, or replace operations. For examples and more information on the SCIM operations format, see the [SCIM specification](https://tools.ietf.org/html/rfc7644#section-3.5.2). |
