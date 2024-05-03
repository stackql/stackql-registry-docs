---
title: orgunits
hide_title: false
hide_table_of_contents: false
keywords:
  - orgunits
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orgunits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.orgunits" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The organizational unit's path name. For example, an organizational unit's name within the /corp/support/sales_support parent path is sales_support. Required. |
| <CopyableCode code="description" /> | `string` | Description of the organizational unit. |
| <CopyableCode code="blockInheritance" /> | `boolean` | Determines if a sub-organizational unit can inherit the settings of the parent organization. The default value is `false`, meaning a sub-organizational unit inherits the settings of the nearest parent organizational unit. We recommend using the default value because setting `block_inheritance` to `true` can have _unintended consequences_. For more information about inheritance and users in an organization structure, see the [administration help center](https://support.google.com/a/answer/4352075). |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="kind" /> | `string` | The type of the API resource. For Orgunits resources, the value is `admin#directory#orgUnit`. |
| <CopyableCode code="orgUnitId" /> | `string` | The unique ID of the organizational unit. |
| <CopyableCode code="orgUnitPath" /> | `string` | The full path to the organizational unit. The `orgUnitPath` is a derived property. When listed, it is derived from `parentOrgunitPath` and organizational unit's `name`. For example, for an organizational unit named 'apps' under parent organization '/engineering', the orgUnitPath is '/engineering/apps'. In order to edit an `orgUnitPath`, either update the name of the organization or the `parentOrgunitPath`. A user's organizational unit determines which Google Workspace services the user has access to. If the user is moved to a new organization, the user's access changes. For more information about organization structures, see the [administration help center](https://support.google.com/a/answer/4352075). For more information about moving a user to a different organization, see [Update a user](/admin-sdk/directory/v1/guides/manage-users.html#update_user). |
| <CopyableCode code="parentOrgUnitId" /> | `string` | The unique ID of the parent organizational unit. Required, unless `parentOrgUnitPath` is set. |
| <CopyableCode code="parentOrgUnitPath" /> | `string` | The organizational unit's parent path. For example, /corp/sales is the parent path for /corp/sales/sales_support organizational unit. Required, unless `parentOrgUnitId` is set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customerId, orgunitsId" /> | Retrieves an organizational unit. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customerId" /> | Retrieves a list of all organizational units for an account. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customerId" /> | Adds an organizational unit. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customerId, orgunitsId" /> | Removes an organizational unit. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customerId" /> | Retrieves a list of all organizational units for an account. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="customerId, orgunitsId" /> | Updates an organizational unit. This method supports [patch semantics](/admin-sdk/directory/v1/guides/performance#patch) |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="customerId, orgunitsId" /> | Updates an organizational unit. |
