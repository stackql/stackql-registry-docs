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
      value: string
    - name: parent
      value: string
    - name: resourceName
      value: string
    - name: state
      value: string
    - name: category
      value: string
    - name: externalUri
      value: string
    - name: sourceProperties
      value: object
    - name: securityMarks
      value:
        - name: name
          value: string
        - name: marks
          value: object
        - name: canonicalName
          value: string
    - name: eventTime
      value: string
    - name: createTime
      value: string
    - name: severity
      value: string
    - name: canonicalName
      value: string
    - name: mute
      value: string
    - name: findingClass
      value: string
    - name: indicator
      value:
        - name: ipAddresses
          value:
            - string
        - name: domains
          value:
            - string
        - name: signatures
          value:
            - - name: memoryHashSignature
                value:
                  - name: binaryFamily
                    value: string
                  - name: detections
                    value:
                      - - name: binary
                          value: string
                        - name: percentPagesMatched
                          value: number
              - name: yaraRuleSignature
                value:
                  - name: yaraRule
                    value: string
              - name: signatureType
                value: string
        - name: uris
          value:
            - string
    - name: vulnerability
      value:
        - name: cve
          value:
            - name: id
              value: string
            - name: references
              value:
                - - name: source
                    value: string
                  - name: uri
                    value: string
            - name: cvssv3
              value:
                - name: baseScore
                  value: number
                - name: attackVector
                  value: string
                - name: attackComplexity
                  value: string
                - name: privilegesRequired
                  value: string
                - name: userInteraction
                  value: string
                - name: scope
                  value: string
                - name: confidentialityImpact
                  value: string
                - name: integrityImpact
                  value: string
                - name: availabilityImpact
                  value: string
            - name: upstreamFixAvailable
              value: boolean
            - name: impact
              value: string
            - name: exploitationActivity
              value: string
            - name: observedInTheWild
              value: boolean
            - name: zeroDay
              value: boolean
            - name: exploitReleaseDate
              value: string
            - name: firstExploitationDate
              value: string
        - name: offendingPackage
          value:
            - name: packageName
              value: string
            - name: cpeUri
              value: string
            - name: packageType
              value: string
            - name: packageVersion
              value: string
        - name: securityBulletin
          value:
            - name: bulletinId
              value: string
            - name: submissionTime
              value: string
            - name: suggestedUpgradeVersion
              value: string
    - name: muteUpdateTime
      value: string
    - name: externalSystems
      value: object
    - name: mitreAttack
      value:
        - name: primaryTactic
          value: string
        - name: primaryTechniques
          value:
            - string
        - name: additionalTactics
          value:
            - string
        - name: additionalTechniques
          value:
            - string
        - name: version
          value: string
    - name: access
      value:
        - name: principalEmail
          value: string
        - name: callerIp
          value: string
        - name: callerIpGeo
          value:
            - name: regionCode
              value: string
        - name: userAgentFamily
          value: string
        - name: userAgent
          value: string
        - name: serviceName
          value: string
        - name: methodName
          value: string
        - name: principalSubject
          value: string
        - name: serviceAccountKeyName
          value: string
        - name: serviceAccountDelegationInfo
          value:
            - - name: principalEmail
                value: string
              - name: principalSubject
                value: string
        - name: userName
          value: string
    - name: connections
      value:
        - - name: destinationIp
            value: string
          - name: destinationPort
            value: integer
          - name: sourceIp
            value: string
          - name: sourcePort
            value: integer
          - name: protocol
            value: string
    - name: muteInitiator
      value: string
    - name: muteInfo
      value:
        - name: staticMute
          value:
            - name: state
              value: string
            - name: applyTime
              value: string
        - name: dynamicMuteRecords
          value:
            - - name: muteConfig
                value: string
              - name: matchTime
                value: string
    - name: processes
      value:
        - - name: name
            value: string
          - name: binary
            value:
              - name: path
                value: string
              - name: size
                value: string
              - name: sha256
                value: string
              - name: hashedSize
                value: string
              - name: partiallyHashed
                value: boolean
              - name: contents
                value: string
              - name: diskPath
                value:
                  - name: partitionUuid
                    value: string
                  - name: relativePath
                    value: string
          - name: libraries
            value:
              - - name: path
                  value: string
                - name: size
                  value: string
                - name: sha256
                  value: string
                - name: hashedSize
                  value: string
                - name: partiallyHashed
                  value: boolean
                - name: contents
                  value: string
          - name: args
            value:
              - string
          - name: argumentsTruncated
            value: boolean
          - name: envVariables
            value:
              - - name: name
                  value: string
                - name: val
                  value: string
          - name: envVariablesTruncated
            value: boolean
          - name: pid
            value: string
          - name: parentPid
            value: string
    - name: contacts
      value: object
    - name: compliances
      value:
        - - name: standard
            value: string
          - name: version
            value: string
          - name: ids
            value:
              - string
    - name: parentDisplayName
      value: string
    - name: description
      value: string
    - name: exfiltration
      value:
        - name: sources
          value:
            - - name: name
                value: string
              - name: components
                value:
                  - string
        - name: targets
          value:
            - - name: name
                value: string
              - name: components
                value:
                  - string
        - name: totalExfiltratedBytes
          value: string
    - name: iamBindings
      value:
        - - name: action
            value: string
          - name: role
            value: string
          - name: member
            value: string
    - name: nextSteps
      value: string
    - name: moduleName
      value: string
    - name: containers
      value:
        - - name: name
            value: string
          - name: uri
            value: string
          - name: imageId
            value: string
          - name: labels
            value:
              - - name: name
                  value: string
                - name: value
                  value: string
          - name: createTime
            value: string
    - name: kubernetes
      value:
        - name: pods
          value:
            - - name: ns
                value: string
              - name: name
                value: string
              - name: labels
                value:
                  - - name: name
                      value: string
                    - name: value
                      value: string
              - name: containers
                value:
                  - - name: name
                      value: string
                    - name: uri
                      value: string
                    - name: imageId
                      value: string
                    - name: labels
                      value:
                        - - name: name
                            value: string
                          - name: value
                            value: string
                    - name: createTime
                      value: string
        - name: nodes
          value:
            - - name: name
                value: string
        - name: nodePools
          value:
            - - name: name
                value: string
              - name: nodes
                value:
                  - - name: name
                      value: string
        - name: roles
          value:
            - - name: kind
                value: string
              - name: ns
                value: string
              - name: name
                value: string
        - name: bindings
          value:
            - - name: ns
                value: string
              - name: name
                value: string
              - name: role
                value:
                  - name: kind
                    value: string
                  - name: ns
                    value: string
                  - name: name
                    value: string
              - name: subjects
                value:
                  - - name: kind
                      value: string
                    - name: ns
                      value: string
                    - name: name
                      value: string
        - name: accessReviews
          value:
            - - name: group
                value: string
              - name: ns
                value: string
              - name: name
                value: string
              - name: resource
                value: string
              - name: subresource
                value: string
              - name: verb
                value: string
              - name: version
                value: string
        - name: objects
          value:
            - - name: group
                value: string
              - name: kind
                value: string
              - name: ns
                value: string
              - name: name
                value: string
              - name: containers
                value:
                  - - name: name
                      value: string
                    - name: uri
                      value: string
                    - name: imageId
                      value: string
                    - name: labels
                      value:
                        - - name: name
                            value: string
                          - name: value
                            value: string
                    - name: createTime
                      value: string
    - name: database
      value:
        - name: name
          value: string
        - name: displayName
          value: string
        - name: userName
          value: string
        - name: query
          value: string
        - name: grantees
          value:
            - string
        - name: version
          value: string
    - name: attackExposure
      value:
        - name: score
          value: number
        - name: latestCalculationTime
          value: string
        - name: attackExposureResult
          value: string
        - name: state
          value: string
        - name: exposedHighValueResourcesCount
          value: integer
        - name: exposedMediumValueResourcesCount
          value: integer
        - name: exposedLowValueResourcesCount
          value: integer
    - name: files
      value:
        - - name: path
            value: string
          - name: size
            value: string
          - name: sha256
            value: string
          - name: hashedSize
            value: string
          - name: partiallyHashed
            value: boolean
          - name: contents
            value: string
    - name: cloudDlpInspection
      value:
        - name: inspectJob
          value: string
        - name: infoType
          value: string
        - name: infoTypeCount
          value: string
        - name: fullScan
          value: boolean
    - name: cloudDlpDataProfile
      value:
        - name: dataProfile
          value: string
        - name: parentType
          value: string
    - name: kernelRootkit
      value:
        - name: name
          value: string
        - name: unexpectedCodeModification
          value: boolean
        - name: unexpectedReadOnlyDataModification
          value: boolean
        - name: unexpectedFtraceHandler
          value: boolean
        - name: unexpectedKprobeHandler
          value: boolean
        - name: unexpectedKernelCodePages
          value: boolean
        - name: unexpectedSystemCallHandler
          value: boolean
        - name: unexpectedInterruptHandler
          value: boolean
        - name: unexpectedProcessesInRunqueue
          value: boolean
    - name: orgPolicies
      value:
        - - name: name
            value: string
    - name: application
      value:
        - name: baseUri
          value: string
        - name: fullUri
          value: string
    - name: backupDisasterRecovery
      value:
        - name: backupTemplate
          value: string
        - name: policies
          value:
            - string
        - name: host
          value: string
        - name: applications
          value:
            - string
        - name: storagePool
          value: string
        - name: policyOptions
          value:
            - string
        - name: profile
          value: string
        - name: appliance
          value: string
        - name: backupType
          value: string
        - name: backupCreateTime
          value: string
    - name: securityPosture
      value:
        - name: name
          value: string
        - name: revisionId
          value: string
        - name: postureDeploymentResource
          value: string
        - name: postureDeployment
          value: string
        - name: changedPolicy
          value: string
        - name: policySet
          value: string
        - name: policy
          value: string
        - name: policyDriftDetails
          value:
            - - name: field
                value: string
              - name: expectedValue
                value: string
              - name: detectedValue
                value: string
    - name: logEntries
      value:
        - - name: cloudLoggingEntry
            value:
              - name: insertId
                value: string
              - name: logId
                value: string
              - name: resourceContainer
                value: string
              - name: timestamp
                value: string
    - name: loadBalancers
      value:
        - - name: name
            value: string
    - name: cloudArmor
      value:
        - name: securityPolicy
          value:
            - name: name
              value: string
            - name: type
              value: string
            - name: preview
              value: boolean
        - name: requests
          value:
            - name: ratio
              value: number
            - name: shortTermAllowed
              value: integer
            - name: longTermAllowed
              value: integer
            - name: longTermDenied
              value: integer
        - name: adaptiveProtection
          value:
            - name: confidence
              value: number
        - name: attack
          value:
            - name: volumePps
              value: integer
            - name: volumeBps
              value: integer
            - name: classification
              value: string
        - name: threatVector
          value: string
        - name: duration
          value: string
    - name: notebook
      value:
        - name: name
          value: string
        - name: service
          value: string
        - name: lastAuthor
          value: string
        - name: notebookUpdateTime
          value: string
    - name: toxicCombination
      value:
        - name: attackExposureScore
          value: number
        - name: relatedFindings
          value:
            - string
    - name: groupMemberships
      value:
        - - name: groupType
            value: string
          - name: groupId
            value: string
    - name: dataAccessEvents
      value:
        - - name: eventId
            value: string
          - name: principalEmail
            value: string
          - name: operation
            value: string
          - name: eventTime
            value: string
    - name: dataFlowEvents
      value:
        - - name: eventId
            value: string
          - name: principalEmail
            value: string
          - name: operation
            value: string
          - name: violatedLocation
            value: string
          - name: eventTime
            value: string

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
