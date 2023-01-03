---
title: users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.scim.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of an external identity |
| `name` | `object` |  |
| `organization_id` | `integer` | The ID of the organization. |
| `emails` | `array` | user emails |
| `externalId` | `string` | The ID of the User. |
| `meta` | `object` |  |
| `displayName` | `string` | The name of the user, suitable for display to end-users |
| `groups` | `array` | associated groups |
| `operations` | `array` | Set of operations to be performed |
| `active` | `boolean` | The active status of the User. |
| `schemas` | `array` | SCIM schema used. |
| `userName` | `string` | Configured by the admin. Could be an email, login, or username |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_provisioning_information_for_user` | `SELECT` | `org, scim_user_id` |  |
| `list_provisioned_identities` | `SELECT` | `org` | Retrieves a paginated list of all provisioned organization members, including pending invitations. If you provide the `filter` parameter, the resources for all matching provisions members are returned.<br /><br />When a user with a SAML-provisioned external identity leaves (or is removed from) an organization, the account's metadata is immediately removed. However, the returned list of user accounts might not always match the organization or enterprise member list you see on GitHub. This can happen in certain cases where an external identity associated with an organization will not match an organization member:<br />  - When a user with a SCIM-provisioned external identity is removed from an organization, the account's metadata is preserved to allow the user to re-join the organization in the future.<br />  - When inviting a user to join an organization, you can expect to see their external identity in the results before they accept the invitation, or if the invitation is cancelled (or never accepted).<br />  - When a user is invited over SCIM, an external identity is created that matches with the invitee's email address. However, this identity is only linked to a user account when the user accepts the invitation by going through SAML SSO.<br /><br />The returned list of external identities can include an entry for a `null` user. These are unlinked SAML identities that are created when a user goes through the following Single Sign-On (SSO) process but does not sign in to their GitHub account after completing SSO:<br /><br />1. The user is granted access by the IdP and is not a member of the GitHub organization.<br /><br />1. The user attempts to access the GitHub organization and initiates the SAML SSO process, and is not currently signed in to their GitHub account.<br /><br />1. After successfully authenticating with the SAML SSO IdP, the `null` external identity entry is created and the user is prompted to sign in to their GitHub account:<br />   - If the user signs in, their GitHub account is linked to this entry.<br />   - If the user does not sign in (or does not create a new account when prompted), they are not added to the GitHub organization, and the external identity `null` entry remains in place. |
| `delete_user_from_org` | `DELETE` | `org, scim_user_id` |  |
| `provision_and_invite_user` | `EXEC` | `org, data__emails, data__name, data__userName` | Provision organization membership for a user, and send an activation email to the email address. |
| `set_information_for_provisioned_user` | `EXEC` | `org, scim_user_id, data__emails, data__name, data__userName` | Replaces an existing provisioned user's information. You must provide all the information required for the user as if you were provisioning them for the first time. Any existing user information that you don't provide will be removed. If you want to only update a specific attribute, use the [Update an attribute for a SCIM user](https://docs.github.com/rest/reference/scim#update-an-attribute-for-a-scim-user) endpoint instead.<br /><br />You must at least provide the required values for the user: `userName`, `name`, and `emails`.<br /><br />**Warning:** Setting `active: false` removes the user from the organization, deletes the external identity, and deletes the associated `{scim_user_id}`. |
| `update_attribute_for_user` | `EXEC` | `org, scim_user_id, data__Operations` | Allows you to change a provisioned user's individual attributes. To change a user's values, you must provide a specific `Operations` JSON format that contains at least one of the `add`, `remove`, or `replace` operations. For examples and more information on the SCIM operations format, see the [SCIM specification](https://tools.ietf.org/html/rfc7644#section-3.5.2).<br /><br />**Note:** Complicated SCIM `path` selectors that include filters are not supported. For example, a `path` selector defined as `"path": "emails[type eq \"work\"]"` will not work.<br /><br />**Warning:** If you set `active:false` using the `replace` operation (as shown in the JSON example below), it removes the user from the organization, deletes the external identity, and deletes the associated `:scim_user_id`.<br /><br />```<br />{<br />  "Operations":[{<br />    "op":"replace",<br />    "value":{<br />      "active":false<br />    }<br />  }]<br />}<br />``` |
