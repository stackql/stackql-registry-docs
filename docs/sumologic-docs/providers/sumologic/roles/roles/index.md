---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
  - roles
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.roles.roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the role. |
| <CopyableCode code="name" /> | `string` | Name of the role. |
| <CopyableCode code="description" /> | `string` | Description of the role. |
| <CopyableCode code="autofillDependencies" /> | `boolean` | Set this to true if you want to automatically append all missing capability requirements. If set to false an error will be thrown if any capabilities are missing their dependencies. |
| <CopyableCode code="capabilities" /> | `array` | List of [capabilities](https://help.sumologic.com/Manage/Users-and-Roles/Manage-Roles/Role-Capabilities) associated with this role. Valid values are<br />### Data Management<br />  - viewCollectors<br />  - manageCollectors<br />  - manageBudgets<br />  - manageDataVolumeFeed<br />  - viewFieldExtraction<br />  - manageFieldExtractionRules<br />  - manageS3DataForwarding<br />  - manageContent<br />  - dataVolumeIndex<br />  - manageConnections<br />  - viewScheduledViews<br />  - manageScheduledViews<br />  - viewPartitions<br />  - managePartitions<br />  - viewFields<br />  - manageFields<br />  - viewAccountOverview<br />  - manageTokens<br />  - downloadSearchResults<br /><br />### Entity management<br />  - manageEntityTypeConfig<br /><br />### Metrics<br />  - metricsTransformation<br />  - metricsExtraction<br />  - metricsRules<br /><br />### Security<br />  - managePasswordPolicy<br />  - ipAllowlisting<br />  - createAccessKeys<br />  - manageAccessKeys<br />  - manageSupportAccountAccess<br />  - manageAuditDataFeed<br />  - manageSaml<br />  - shareDashboardOutsideOrg<br />  - manageOrgSettings<br />  - changeDataAccessLevel<br /><br />### Dashboards<br />  - shareDashboardWorld<br />  - shareDashboardAllowlist<br /><br />### UserManagement<br />  - manageUsersAndRoles<br /><br />### Observability<br />  - searchAuditIndex<br />  - auditEventIndex<br /><br />### Cloud SIEM Enterprise<br />  - viewCse<br /><br />### Alerting<br />  - viewMonitorsV2<br />  - manageMonitorsV2<br />  - viewAlerts |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the resource. |
| <CopyableCode code="filterPredicate" /> | `string` | A search filter to restrict access to specific logs. The filter is silently added to the beginning of each query a user runs. For example, using '!_sourceCategory=billing' as a filter predicate will prevent users assigned to the role from viewing logs from the source category named 'billing'. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="systemDefined" /> | `boolean` | Role is system or user defined. |
| <CopyableCode code="users" /> | `array` | List of user identifiers to assign the role to. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getRole" /> | `SELECT` | <CopyableCode code="id, region" /> | Get a role with the given identifier in the organization. |
| <CopyableCode code="listRoles" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of all the roles in the organization. The response is paginated with a default limit of 100 roles per page. |
| <CopyableCode code="createRole" /> | `INSERT` | <CopyableCode code="data__name, region" /> | Create a new role in the organization. |
| <CopyableCode code="deleteRole" /> | `DELETE` | <CopyableCode code="id, region" /> | Delete a role with the given identifier from the organization. |
| <CopyableCode code="updateRole" /> | `EXEC` | <CopyableCode code="id, data__capabilities, data__description, data__filterPredicate, data__name, data__users, region" /> | Update an existing role in the organization. |
