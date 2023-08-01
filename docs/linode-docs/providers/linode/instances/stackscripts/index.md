---
title: stackscripts
hide_title: false
hide_table_of_contents: false
keywords:
  - stackscripts
  - instances
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
<tr><td><b>Name</b></td><td><code>stackscripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.instances.stackscripts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique ID of this StackScript. |
| `description` | `string` | A description for the StackScript.<br /> |
| `deployments_active` | `integer` | Count of currently active, deployed Linodes created from this StackScript.<br /> |
| `images` | `array` | An array of Image IDs. These are the Images that can be deployed with this StackScript.<br /><br />`any/all` indicates that all available Images, including private Images, are accepted.<br /> |
| `user_defined_fields` | `array` | This is a list of fields defined with a special syntax inside this StackScript that allow for supplying customized parameters during deployment. See [Declare User-Defined Fields (UDFs)](/docs/products/tools/stackscripts/guides/write-a-custom-script/#declare-user-defined-fields-udfs) for more information.<br /> |
| `rev_note` | `string` | This field allows you to add notes for the set of revisions made to this StackScript.<br /> |
| `username` | `string` | The User who created the StackScript.<br /> |
| `is_public` | `boolean` | This determines whether other users can use your StackScript. **Once a StackScript is made public, it cannot be made private.**<br /> |
| `script` | `string` | The script to execute when provisioning a new Linode with this StackScript.<br /> |
| `deployments_total` | `integer` | The total number of times this StackScript has been deployed.<br /> |
| `mine` | `boolean` | Returns `true` if this StackScript is owned by the account of the user making the request, and the user<br />making the request is unrestricted or has access to this StackScript.<br /> |
| `updated` | `string` | The date this StackScript was last updated.<br /> |
| `created` | `string` | The date this StackScript was created.<br /> |
| `label` | `string` | The StackScript's label is for display purposes only.<br /> |
| `user_gravatar_id` | `string` | The Gravatar ID for the User who created the StackScript.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getStackScript` | `SELECT` | `stackscriptId` | Returns all of the information about a specified StackScript, including the contents of the script.<br /> |
| `getStackScripts` | `SELECT` |  | If the request is not authenticated, only public StackScripts are returned.<br /><br />For more information on StackScripts, please read our [StackScripts documentation](/docs/products/tools/stackscripts/).<br /> |
| `addStackScript` | `INSERT` | `data__images, data__label, data__script` | Creates a StackScript in your Account.<br /> |
| `deleteStackScript` | `DELETE` | `stackscriptId` | Deletes a private StackScript you have permission to `read_write`. You cannot delete a public StackScript.<br /> |
| `_getStackScript` | `EXEC` | `stackscriptId` | Returns all of the information about a specified StackScript, including the contents of the script.<br /> |
| `_getStackScripts` | `EXEC` |  | If the request is not authenticated, only public StackScripts are returned.<br /><br />For more information on StackScripts, please read our [StackScripts documentation](/docs/products/tools/stackscripts/).<br /> |
| `updateStackScript` | `EXEC` | `stackscriptId` | Updates a StackScript.<br /><br />**Once a StackScript is made public, it cannot be made private.**<br /> |
