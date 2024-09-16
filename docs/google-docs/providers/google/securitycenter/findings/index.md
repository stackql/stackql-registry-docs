---
title: findings
hide_title: false
hide_table_of_contents: false
keywords:
  - findings
  - securitycenter
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>findings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>findings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.findings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="finding" /> | `object` | Security Command Center finding. A finding is a record of assessment data like security, risk, health, or privacy, that is ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, a cross-site scripting (XSS) vulnerability in an App Engine application is a finding. |
| <CopyableCode code="resource" /> | `object` | Information related to the Google Cloud resource that is associated with this finding. |
| <CopyableCode code="stateChange" /> | `string` | State change of the finding between the points in time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_sources_findings_list" /> | `SELECT` | <CopyableCode code="foldersId, sourcesId" /> | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings |
| <CopyableCode code="organizations_sources_findings_list" /> | `SELECT` | <CopyableCode code="organizationsId, sourcesId" /> | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings |
| <CopyableCode code="projects_sources_findings_list" /> | `SELECT` | <CopyableCode code="projectsId, sourcesId" /> | Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings |
| <CopyableCode code="organizations_sources_findings_create" /> | `INSERT` | <CopyableCode code="organizationsId, sourcesId" /> | Creates a finding. The corresponding source must exist for finding creation to succeed. |
| <CopyableCode code="folders_sources_findings_patch" /> | `UPDATE` | <CopyableCode code="findingsId, foldersId, sourcesId" /> | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| <CopyableCode code="organizations_sources_findings_patch" /> | `UPDATE` | <CopyableCode code="findingsId, organizationsId, sourcesId" /> | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| <CopyableCode code="projects_sources_findings_patch" /> | `UPDATE` | <CopyableCode code="findingsId, projectsId, sourcesId" /> | Creates or updates a finding. The corresponding source must exist for a finding creation to succeed. |
| <CopyableCode code="folders_findings_bulk_mute" /> | `EXEC` | <CopyableCode code="foldersId" /> | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| <CopyableCode code="folders_sources_findings_group" /> | `EXEC` | <CopyableCode code="foldersId, sourcesId" /> | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings, /v1/folders/{folder_id}/sources/-/findings, /v1/projects/{project_id}/sources/-/findings |
| <CopyableCode code="folders_sources_findings_set_mute" /> | `EXEC` | <CopyableCode code="findingsId, foldersId, sourcesId" /> | Updates the mute state of a finding. |
| <CopyableCode code="folders_sources_findings_set_state" /> | `EXEC` | <CopyableCode code="findingsId, foldersId, sourcesId" /> | Updates the state of a finding. |
| <CopyableCode code="organizations_findings_bulk_mute" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| <CopyableCode code="organizations_sources_findings_group" /> | `EXEC` | <CopyableCode code="organizationsId, sourcesId" /> | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings, /v1/folders/{folder_id}/sources/-/findings, /v1/projects/{project_id}/sources/-/findings |
| <CopyableCode code="organizations_sources_findings_set_mute" /> | `EXEC` | <CopyableCode code="findingsId, organizationsId, sourcesId" /> | Updates the mute state of a finding. |
| <CopyableCode code="organizations_sources_findings_set_state" /> | `EXEC` | <CopyableCode code="findingsId, organizationsId, sourcesId" /> | Updates the state of a finding. |
| <CopyableCode code="projects_findings_bulk_mute" /> | `EXEC` | <CopyableCode code="projectsId" /> | Kicks off an LRO to bulk mute findings for a parent based on a filter. The parent can be either an organization, folder or project. The findings matched by the filter will be muted after the LRO is done. |
| <CopyableCode code="projects_sources_findings_group" /> | `EXEC` | <CopyableCode code="projectsId, sourcesId" /> | Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings, /v1/folders/{folder_id}/sources/-/findings, /v1/projects/{project_id}/sources/-/findings |
| <CopyableCode code="projects_sources_findings_set_mute" /> | `EXEC` | <CopyableCode code="findingsId, projectsId, sourcesId" /> | Updates the mute state of a finding. |
| <CopyableCode code="projects_sources_findings_set_state" /> | `EXEC` | <CopyableCode code="findingsId, projectsId, sourcesId" /> | Updates the state of a finding. |

## `SELECT` examples

Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings

```sql
SELECT
finding,
resource,
stateChange
FROM google.securitycenter.findings
WHERE foldersId = '{{ foldersId }}'
AND sourcesId = '{{ sourcesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>findings</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.securitycenter.findings (
organizationsId,
sourcesId,
name,
parent,
resourceName,
state,
category,
externalUri,
sourceProperties,
securityMarks,
eventTime,
createTime,
severity,
canonicalName,
mute,
findingClass,
indicator,
vulnerability,
muteUpdateTime,
externalSystems,
mitreAttack,
access,
connections,
muteInitiator,
muteInfo,
processes,
contacts,
compliances,
parentDisplayName,
description,
exfiltration,
iamBindings,
nextSteps,
moduleName,
containers,
kubernetes,
database,
attackExposure,
files,
cloudDlpInspection,
cloudDlpDataProfile,
kernelRootkit,
orgPolicies,
application,
backupDisasterRecovery,
securityPosture,
logEntries,
loadBalancers,
cloudArmor,
notebook,
toxicCombination,
groupMemberships,
dataAccessEvents,
dataFlowEvents
)
SELECT 
'{{ organizationsId }}',
'{{ sourcesId }}',
'{{ name }}',
'{{ parent }}',
'{{ resourceName }}',
'{{ state }}',
'{{ category }}',
'{{ externalUri }}',
'{{ sourceProperties }}',
'{{ securityMarks }}',
'{{ eventTime }}',
'{{ createTime }}',
'{{ severity }}',
'{{ canonicalName }}',
'{{ mute }}',
'{{ findingClass }}',
'{{ indicator }}',
'{{ vulnerability }}',
'{{ muteUpdateTime }}',
'{{ externalSystems }}',
'{{ mitreAttack }}',
'{{ access }}',
'{{ connections }}',
'{{ muteInitiator }}',
'{{ muteInfo }}',
'{{ processes }}',
'{{ contacts }}',
'{{ compliances }}',
'{{ parentDisplayName }}',
'{{ description }}',
'{{ exfiltration }}',
'{{ iamBindings }}',
'{{ nextSteps }}',
'{{ moduleName }}',
'{{ containers }}',
'{{ kubernetes }}',
'{{ database }}',
'{{ attackExposure }}',
'{{ files }}',
'{{ cloudDlpInspection }}',
'{{ cloudDlpDataProfile }}',
'{{ kernelRootkit }}',
'{{ orgPolicies }}',
'{{ application }}',
'{{ backupDisasterRecovery }}',
'{{ securityPosture }}',
'{{ logEntries }}',
'{{ loadBalancers }}',
'{{ cloudArmor }}',
'{{ notebook }}',
'{{ toxicCombination }}',
'{{ groupMemberships }}',
'{{ dataAccessEvents }}',
'{{ dataFlowEvents }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: parent
      value: '{{ parent }}'
    - name: resourceName
      value: '{{ resourceName }}'
    - name: state
      value: '{{ state }}'
    - name: category
      value: '{{ category }}'
    - name: externalUri
      value: '{{ externalUri }}'
    - name: sourceProperties
      value: '{{ sourceProperties }}'
    - name: securityMarks
      value: '{{ securityMarks }}'
    - name: eventTime
      value: '{{ eventTime }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: severity
      value: '{{ severity }}'
    - name: canonicalName
      value: '{{ canonicalName }}'
    - name: mute
      value: '{{ mute }}'
    - name: findingClass
      value: '{{ findingClass }}'
    - name: indicator
      value: '{{ indicator }}'
    - name: vulnerability
      value: '{{ vulnerability }}'
    - name: muteUpdateTime
      value: '{{ muteUpdateTime }}'
    - name: externalSystems
      value: '{{ externalSystems }}'
    - name: mitreAttack
      value: '{{ mitreAttack }}'
    - name: access
      value: '{{ access }}'
    - name: connections
      value: '{{ connections }}'
    - name: muteInitiator
      value: '{{ muteInitiator }}'
    - name: muteInfo
      value: '{{ muteInfo }}'
    - name: processes
      value: '{{ processes }}'
    - name: contacts
      value: '{{ contacts }}'
    - name: compliances
      value: '{{ compliances }}'
    - name: parentDisplayName
      value: '{{ parentDisplayName }}'
    - name: description
      value: '{{ description }}'
    - name: exfiltration
      value: '{{ exfiltration }}'
    - name: iamBindings
      value: '{{ iamBindings }}'
    - name: nextSteps
      value: '{{ nextSteps }}'
    - name: moduleName
      value: '{{ moduleName }}'
    - name: containers
      value: '{{ containers }}'
    - name: kubernetes
      value: '{{ kubernetes }}'
    - name: database
      value: '{{ database }}'
    - name: attackExposure
      value: '{{ attackExposure }}'
    - name: files
      value: '{{ files }}'
    - name: cloudDlpInspection
      value: '{{ cloudDlpInspection }}'
    - name: cloudDlpDataProfile
      value: '{{ cloudDlpDataProfile }}'
    - name: kernelRootkit
      value: '{{ kernelRootkit }}'
    - name: orgPolicies
      value: '{{ orgPolicies }}'
    - name: application
      value: '{{ application }}'
    - name: backupDisasterRecovery
      value: '{{ backupDisasterRecovery }}'
    - name: securityPosture
      value: '{{ securityPosture }}'
    - name: logEntries
      value: '{{ logEntries }}'
    - name: loadBalancers
      value: '{{ loadBalancers }}'
    - name: cloudArmor
      value: '{{ cloudArmor }}'
    - name: notebook
      value: '{{ notebook }}'
    - name: toxicCombination
      value: '{{ toxicCombination }}'
    - name: groupMemberships
      value: '{{ groupMemberships }}'
    - name: dataAccessEvents
      value: '{{ dataAccessEvents }}'
    - name: dataFlowEvents
      value: '{{ dataFlowEvents }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>findings</code> resource.

```sql
/*+ update */
UPDATE google.securitycenter.findings
SET 
name = '{{ name }}',
parent = '{{ parent }}',
resourceName = '{{ resourceName }}',
state = '{{ state }}',
category = '{{ category }}',
externalUri = '{{ externalUri }}',
sourceProperties = '{{ sourceProperties }}',
securityMarks = '{{ securityMarks }}',
eventTime = '{{ eventTime }}',
createTime = '{{ createTime }}',
severity = '{{ severity }}',
canonicalName = '{{ canonicalName }}',
mute = '{{ mute }}',
findingClass = '{{ findingClass }}',
indicator = '{{ indicator }}',
vulnerability = '{{ vulnerability }}',
muteUpdateTime = '{{ muteUpdateTime }}',
externalSystems = '{{ externalSystems }}',
mitreAttack = '{{ mitreAttack }}',
access = '{{ access }}',
connections = '{{ connections }}',
muteInitiator = '{{ muteInitiator }}',
muteInfo = '{{ muteInfo }}',
processes = '{{ processes }}',
contacts = '{{ contacts }}',
compliances = '{{ compliances }}',
parentDisplayName = '{{ parentDisplayName }}',
description = '{{ description }}',
exfiltration = '{{ exfiltration }}',
iamBindings = '{{ iamBindings }}',
nextSteps = '{{ nextSteps }}',
moduleName = '{{ moduleName }}',
containers = '{{ containers }}',
kubernetes = '{{ kubernetes }}',
database = '{{ database }}',
attackExposure = '{{ attackExposure }}',
files = '{{ files }}',
cloudDlpInspection = '{{ cloudDlpInspection }}',
cloudDlpDataProfile = '{{ cloudDlpDataProfile }}',
kernelRootkit = '{{ kernelRootkit }}',
orgPolicies = '{{ orgPolicies }}',
application = '{{ application }}',
backupDisasterRecovery = '{{ backupDisasterRecovery }}',
securityPosture = '{{ securityPosture }}',
logEntries = '{{ logEntries }}',
loadBalancers = '{{ loadBalancers }}',
cloudArmor = '{{ cloudArmor }}',
notebook = '{{ notebook }}',
toxicCombination = '{{ toxicCombination }}',
groupMemberships = '{{ groupMemberships }}',
dataAccessEvents = '{{ dataAccessEvents }}',
dataFlowEvents = '{{ dataFlowEvents }}'
WHERE 
findingsId = '{{ findingsId }}'
AND foldersId = '{{ foldersId }}'
AND sourcesId = '{{ sourcesId }}';
```
