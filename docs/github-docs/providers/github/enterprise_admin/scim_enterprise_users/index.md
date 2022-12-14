---
title: scim_enterprise_users
hide_title: false
hide_table_of_contents: false
keywords:
  - scim_enterprise_users
  - enterprise_admin
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scim_enterprise_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.scim_enterprise_users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `object` |
| `emails` | `array` |
| `externalId` | `string` |
| `groups` | `array` |
| `active` | `boolean` |
| `userName` | `string` |
| `schemas` | `array` |
| `meta` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_provisioning_information_for_enterprise_user` | `SELECT` | `enterprise, scim_user_id` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change. |
| `list_provisioned_identities_enterprise` | `SELECT` | `enterprise` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change.<br /><br />Retrieves a paginated list of all provisioned enterprise members, including pending invitations.<br /><br />When a user with a SAML-provisioned external identity leaves (or is removed from) an enterprise, the account's metadata is immediately removed. However, the returned list of user accounts might not always match the organization or enterprise member list you see on GitHub. This can happen in certain cases where an external identity associated with an organization will not match an organization member:<br />  - When a user with a SCIM-provisioned external identity is removed from an enterprise, the account's metadata is preserved to allow the user to re-join the organization in the future.<br />  - When inviting a user to join an organization, you can expect to see their external identity in the results before they accept the invitation, or if the invitation is cancelled (or never accepted).<br />  - When a user is invited over SCIM, an external identity is created that matches with the invitee's email address. However, this identity is only linked to a user account when the user accepts the invitation by going through SAML SSO.<br /><br />The returned list of external identities can include an entry for a `null` user. These are unlinked SAML identities that are created when a user goes through the following Single Sign-On (SSO) process but does not sign in to their GitHub account after completing SSO:<br /><br />1. The user is granted access by the IdP and is not a member of the GitHub enterprise.<br /><br />1. The user attempts to access the GitHub enterprise and initiates the SAML SSO process, and is not currently signed in to their GitHub account.<br /><br />1. After successfully authenticating with the SAML SSO IdP, the `null` external identity entry is created and the user is prompted to sign in to their GitHub account:<br />   - If the user signs in, their GitHub account is linked to this entry.<br />   - If the user does not sign in (or does not create a new account when prompted), they are not added to the GitHub enterprise, and the external identity `null` entry remains in place. |
| `provision_and_invite_enterprise_user` | `INSERT` | `enterprise, data__emails, data__name, data__schemas, data__userName` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change.<br /><br />Provision enterprise membership for a user, and send organization invitation emails to the email address.<br /><br />You can optionally include the groups a user will be invited to join. If you do not provide a list of `groups`, the user is provisioned for the enterprise, but no organization invitation emails will be sent. |
| `delete_user_from_enterprise` | `DELETE` | `enterprise, scim_user_id` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change. |
| `set_information_for_provisioned_enterprise_user` | `EXEC` | `enterprise, scim_user_id, data__emails, data__name, data__schemas, data__userName` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change.<br /><br />Replaces an existing provisioned user's information. You must provide all the information required for the user as if you were provisioning them for the first time. Any existing user information that you don't provide will be removed. If you want to only update a specific attribute, use the [Update an attribute for a SCIM user](#update-an-attribute-for-an-enterprise-scim-user) endpoint instead.<br /><br />You must at least provide the required values for the user: `userName`, `name`, and `emails`.<br /><br />**Warning:** Setting `active: false` removes the user from the enterprise, deletes the external identity, and deletes the associated `&#123;scim_user_id&#125;`. |
| `update_attribute_for_enterprise_user` | `EXEC` | `enterprise, scim_user_id, data__Operations, data__schemas` | **Note:** The SCIM API endpoints for enterprise accounts are currently in beta and are subject to change.<br /><br />Allows you to change a provisioned user's individual attributes. To change a user's values, you must provide a specific `Operations` JSON format that contains at least one of the `add`, `remove`, or `replace` operations. For examples and more information on the SCIM operations format, see the [SCIM specification](https://tools.ietf.org/html/rfc7644#section-3.5.2).<br /><br />**Note:** Complicated SCIM `path` selectors that include filters are not supported. For example, a `path` selector defined as `"path": "emails[type eq \"work\"]"` will not work.<br /><br />**Warning:** If you set `active:false` using the `replace` operation (as shown in the JSON example below), it removes the user from the enterprise, deletes the external identity, and deletes the associated `:scim_user_id`.<br /><br />```<br />&#123;<br />  "Operations":[&#123;<br />    "op":"replace",<br />    "value":&#123;<br />      "active":false<br />    &#125;<br />  &#125;]<br />&#125;<br />``` |
