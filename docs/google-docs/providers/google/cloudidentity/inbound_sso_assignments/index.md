---
title: inbound_sso_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - inbound_sso_assignments
  - cloudidentity
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inbound_sso_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.inbound_sso_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Inbound SSO Assignment. |
| `targetOrgUnit` | `string` | Immutable. Must be of the form `orgUnits/&#123;org_unit&#125;`. |
| `customer` | `string` | Immutable. The customer. For example: `customers/C0123abc`. |
| `rank` | `integer` | Must be zero (which is the default value so it can be omitted) for assignments with `target_org_unit` set and must be greater-than-or-equal-to one for assignments with `target_group` set. |
| `samlSsoInfo` | `object` | Details that are applicable when `sso_mode` == `SAML_SSO`. |
| `signInBehavior` | `object` | Controls sign-in behavior. |
| `ssoMode` | `string` | Inbound SSO behavior. |
| `targetGroup` | `string` | Immutable. Must be of the form `groups/&#123;group&#125;`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `inboundSsoAssignmentsId` | Gets an InboundSsoAssignment. |
| `list` | `SELECT` |  | Lists the InboundSsoAssignments for a `Customer`. |
| `create` | `INSERT` |  | Creates an InboundSsoAssignment for users and devices in a `Customer` under a given `Group` or `OrgUnit`. |
| `delete` | `DELETE` | `inboundSsoAssignmentsId` | Deletes an InboundSsoAssignment. To disable SSO, Create (or Update) an assignment that has `sso_mode` == `SSO_OFF`. |
| `_list` | `EXEC` |  | Lists the InboundSsoAssignments for a `Customer`. |
| `patch` | `EXEC` | `inboundSsoAssignmentsId` | Updates an InboundSsoAssignment. The body of this request is the `inbound_sso_assignment` field and the `update_mask` is relative to that. For example: a PATCH to `/v1/inboundSsoAssignments/0abcdefg1234567&update_mask=rank` with a body of `&#123; "rank": 1 &#125;` moves that (presumably group-targeted) SSO assignment to the highest priority and shifts any other group-targeted assignments down in priority. |
