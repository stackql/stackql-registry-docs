---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - managed
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.managed.contacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This Contact's unique ID.<br /> |
| <CopyableCode code="name" /> | `string` | The name of this Contact.<br /> |
| <CopyableCode code="email" /> | `string` | The address to email this Contact to alert them of issues.<br /> |
| <CopyableCode code="group" /> | `string` | A grouping for this Contact. This is for display purposes only.<br /> |
| <CopyableCode code="phone" /> | `object` | Information about how to reach this Contact by phone.<br /> |
| <CopyableCode code="updated" /> | `string` | When this Contact was last updated.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getManagedContact" /> | `SELECT` | <CopyableCode code="contactId" /> | Returns a single Managed Contact.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="getManagedContacts" /> | `SELECT` |  | Returns a paginated list of Managed Contacts on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="createManagedContact" /> | `INSERT` |  | Creates a Managed Contact.  A Managed Contact is someone Linode<br />special forces can contact in the course of attempting to resolve an issue<br />with a Managed Service.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="deleteManagedContact" /> | `DELETE` | <CopyableCode code="contactId" /> | Deletes a Managed Contact.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="_getManagedContact" /> | `EXEC` | <CopyableCode code="contactId" /> | Returns a single Managed Contact.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="_getManagedContacts" /> | `EXEC` |  | Returns a paginated list of Managed Contacts on your Account.<br /><br />This command can only be accessed by the unrestricted users of an account.<br /> |
| <CopyableCode code="updateManagedContact" /> | `EXEC` | <CopyableCode code="contactId" /> | Updates information about a Managed Contact.<br />This command can only be accessed by the unrestricted users of an account.<br /> |
