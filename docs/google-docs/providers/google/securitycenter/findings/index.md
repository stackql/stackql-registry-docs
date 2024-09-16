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
eventTime,
severity,
canonicalName,
mute,
findingClass,
indicator,
vulnerability,
mitreAttack,
access,
connections,
muteInitiator,
processes,
compliances,
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
'{{ eventTime }}',
'{{ severity }}',
'{{ canonicalName }}',
'{{ mute }}',
'{{ findingClass }}',
'{{ indicator }}',
'{{ vulnerability }}',
'{{ mitreAttack }}',
'{{ access }}',
'{{ connections }}',
'{{ muteInitiator }}',
'{{ processes }}',
'{{ compliances }}',
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
    - name: eventTime
      value: '{{ eventTime }}'
    - name: severity
      value: '{{ severity }}'
    - name: canonicalName
      value: '{{ canonicalName }}'
    - name: mute
      value: '{{ mute }}'
    - name: findingClass
      value: '{{ findingClass }}'
    - name: indicator
      value:
        - name: ipAddresses
          value:
            - name: type
              value: '{{ type }}'
        - name: domains
          value:
            - name: type
              value: '{{ type }}'
        - name: signatures
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: uris
          value:
            - name: type
              value: '{{ type }}'
    - name: vulnerability
      value:
        - name: cve
          value:
            - name: references
              value:
                - name: $ref
                  value: '{{ $ref }}'
            - name: cvssv3
              value:
                - name: baseScore
                  value: '{{ baseScore }}'
                - name: attackVector
                  value: '{{ attackVector }}'
                - name: attackComplexity
                  value: '{{ attackComplexity }}'
                - name: privilegesRequired
                  value: '{{ privilegesRequired }}'
                - name: userInteraction
                  value: '{{ userInteraction }}'
                - name: scope
                  value: '{{ scope }}'
                - name: confidentialityImpact
                  value: '{{ confidentialityImpact }}'
                - name: integrityImpact
                  value: '{{ integrityImpact }}'
                - name: availabilityImpact
                  value: '{{ availabilityImpact }}'
            - name: upstreamFixAvailable
              value: '{{ upstreamFixAvailable }}'
            - name: impact
              value: '{{ impact }}'
            - name: exploitationActivity
              value: '{{ exploitationActivity }}'
            - name: observedInTheWild
              value: '{{ observedInTheWild }}'
            - name: zeroDay
              value: '{{ zeroDay }}'
            - name: exploitReleaseDate
              value: '{{ exploitReleaseDate }}'
            - name: firstExploitationDate
              value: '{{ firstExploitationDate }}'
        - name: offendingPackage
          value:
            - name: packageName
              value: '{{ packageName }}'
            - name: cpeUri
              value: '{{ cpeUri }}'
            - name: packageType
              value: '{{ packageType }}'
            - name: packageVersion
              value: '{{ packageVersion }}'
        - name: securityBulletin
          value:
            - name: bulletinId
              value: '{{ bulletinId }}'
            - name: submissionTime
              value: '{{ submissionTime }}'
            - name: suggestedUpgradeVersion
              value: '{{ suggestedUpgradeVersion }}'
    - name: mitreAttack
      value:
        - name: primaryTactic
          value: '{{ primaryTactic }}'
        - name: primaryTechniques
          value:
            - name: type
              value: '{{ type }}'
            - name: enumDescriptions
              value: '{{ enumDescriptions }}'
            - name: enum
              value: '{{ enum }}'
        - name: additionalTactics
          value:
            - name: type
              value: '{{ type }}'
            - name: enumDescriptions
              value: '{{ enumDescriptions }}'
            - name: enum
              value: '{{ enum }}'
        - name: additionalTechniques
          value:
            - name: type
              value: '{{ type }}'
            - name: enumDescriptions
              value: '{{ enumDescriptions }}'
            - name: enum
              value: '{{ enum }}'
        - name: version
          value: '{{ version }}'
    - name: access
      value:
        - name: principalEmail
          value: '{{ principalEmail }}'
        - name: callerIp
          value: '{{ callerIp }}'
        - name: callerIpGeo
          value:
            - name: regionCode
              value: '{{ regionCode }}'
        - name: userAgentFamily
          value: '{{ userAgentFamily }}'
        - name: userAgent
          value: '{{ userAgent }}'
        - name: serviceName
          value: '{{ serviceName }}'
        - name: methodName
          value: '{{ methodName }}'
        - name: principalSubject
          value: '{{ principalSubject }}'
        - name: serviceAccountKeyName
          value: '{{ serviceAccountKeyName }}'
        - name: serviceAccountDelegationInfo
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: userName
          value: '{{ userName }}'
    - name: connections
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: muteInitiator
      value: '{{ muteInitiator }}'
    - name: processes
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: compliances
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: description
      value: '{{ description }}'
    - name: exfiltration
      value:
        - name: sources
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: targets
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: totalExfiltratedBytes
          value: '{{ totalExfiltratedBytes }}'
    - name: iamBindings
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: nextSteps
      value: '{{ nextSteps }}'
    - name: moduleName
      value: '{{ moduleName }}'
    - name: containers
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: kubernetes
      value:
        - name: pods
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: nodes
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: nodePools
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: roles
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: bindings
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: accessReviews
          value:
            - name: $ref
              value: '{{ $ref }}'
        - name: objects
          value:
            - name: $ref
              value: '{{ $ref }}'
    - name: database
      value:
        - name: name
          value: '{{ name }}'
        - name: displayName
          value: '{{ displayName }}'
        - name: userName
          value: '{{ userName }}'
        - name: query
          value: '{{ query }}'
        - name: grantees
          value:
            - name: type
              value: '{{ type }}'
        - name: version
          value: '{{ version }}'
    - name: attackExposure
      value:
        - name: score
          value: '{{ score }}'
        - name: latestCalculationTime
          value: '{{ latestCalculationTime }}'
        - name: attackExposureResult
          value: '{{ attackExposureResult }}'
        - name: state
          value: '{{ state }}'
        - name: exposedHighValueResourcesCount
          value: '{{ exposedHighValueResourcesCount }}'
        - name: exposedMediumValueResourcesCount
          value: '{{ exposedMediumValueResourcesCount }}'
        - name: exposedLowValueResourcesCount
          value: '{{ exposedLowValueResourcesCount }}'
    - name: files
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: cloudDlpInspection
      value:
        - name: inspectJob
          value: '{{ inspectJob }}'
        - name: infoType
          value: '{{ infoType }}'
        - name: infoTypeCount
          value: '{{ infoTypeCount }}'
        - name: fullScan
          value: '{{ fullScan }}'
    - name: cloudDlpDataProfile
      value:
        - name: dataProfile
          value: '{{ dataProfile }}'
        - name: parentType
          value: '{{ parentType }}'
    - name: kernelRootkit
      value:
        - name: name
          value: '{{ name }}'
        - name: unexpectedCodeModification
          value: '{{ unexpectedCodeModification }}'
        - name: unexpectedReadOnlyDataModification
          value: '{{ unexpectedReadOnlyDataModification }}'
        - name: unexpectedFtraceHandler
          value: '{{ unexpectedFtraceHandler }}'
        - name: unexpectedKprobeHandler
          value: '{{ unexpectedKprobeHandler }}'
        - name: unexpectedKernelCodePages
          value: '{{ unexpectedKernelCodePages }}'
        - name: unexpectedSystemCallHandler
          value: '{{ unexpectedSystemCallHandler }}'
        - name: unexpectedInterruptHandler
          value: '{{ unexpectedInterruptHandler }}'
        - name: unexpectedProcessesInRunqueue
          value: '{{ unexpectedProcessesInRunqueue }}'
    - name: orgPolicies
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: application
      value:
        - name: baseUri
          value: '{{ baseUri }}'
        - name: fullUri
          value: '{{ fullUri }}'
    - name: backupDisasterRecovery
      value:
        - name: backupTemplate
          value: '{{ backupTemplate }}'
        - name: policies
          value:
            - name: type
              value: '{{ type }}'
        - name: host
          value: '{{ host }}'
        - name: applications
          value:
            - name: type
              value: '{{ type }}'
        - name: storagePool
          value: '{{ storagePool }}'
        - name: policyOptions
          value:
            - name: type
              value: '{{ type }}'
        - name: profile
          value: '{{ profile }}'
        - name: appliance
          value: '{{ appliance }}'
        - name: backupType
          value: '{{ backupType }}'
        - name: backupCreateTime
          value: '{{ backupCreateTime }}'
    - name: securityPosture
      value:
        - name: name
          value: '{{ name }}'
        - name: revisionId
          value: '{{ revisionId }}'
        - name: postureDeploymentResource
          value: '{{ postureDeploymentResource }}'
        - name: postureDeployment
          value: '{{ postureDeployment }}'
        - name: changedPolicy
          value: '{{ changedPolicy }}'
        - name: policySet
          value: '{{ policySet }}'
        - name: policy
          value: '{{ policy }}'
        - name: policyDriftDetails
          value:
            - name: $ref
              value: '{{ $ref }}'
    - name: logEntries
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: loadBalancers
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: cloudArmor
      value:
        - name: securityPolicy
          value:
            - name: name
              value: '{{ name }}'
            - name: type
              value: '{{ type }}'
            - name: preview
              value: '{{ preview }}'
        - name: requests
          value:
            - name: ratio
              value: '{{ ratio }}'
            - name: shortTermAllowed
              value: '{{ shortTermAllowed }}'
            - name: longTermAllowed
              value: '{{ longTermAllowed }}'
            - name: longTermDenied
              value: '{{ longTermDenied }}'
        - name: adaptiveProtection
          value:
            - name: confidence
              value: '{{ confidence }}'
        - name: attack
          value:
            - name: volumePps
              value: '{{ volumePps }}'
            - name: volumeBps
              value: '{{ volumeBps }}'
            - name: classification
              value: '{{ classification }}'
        - name: threatVector
          value: '{{ threatVector }}'
        - name: duration
          value: '{{ duration }}'
    - name: notebook
      value:
        - name: name
          value: '{{ name }}'
        - name: service
          value: '{{ service }}'
        - name: lastAuthor
          value: '{{ lastAuthor }}'
        - name: notebookUpdateTime
          value: '{{ notebookUpdateTime }}'
    - name: toxicCombination
      value:
        - name: attackExposureScore
          value: '{{ attackExposureScore }}'
        - name: relatedFindings
          value:
            - name: type
              value: '{{ type }}'
    - name: groupMemberships
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: dataAccessEvents
      value:
        - name: $ref
          value: '{{ $ref }}'
    - name: dataFlowEvents
      value:
        - name: $ref
          value: '{{ $ref }}'

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
eventTime = '{{ eventTime }}',
severity = '{{ severity }}',
canonicalName = '{{ canonicalName }}',
mute = '{{ mute }}',
findingClass = '{{ findingClass }}',
indicator = '{{ indicator }}',
vulnerability = '{{ vulnerability }}',
mitreAttack = '{{ mitreAttack }}',
access = '{{ access }}',
connections = '{{ connections }}',
muteInitiator = '{{ muteInitiator }}',
processes = '{{ processes }}',
compliances = '{{ compliances }}',
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
