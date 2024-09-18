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
name: string
parent: string
resourceName: string
state: string
category: string
externalUri: string
sourceProperties: object
securityMarks:
  name: string
  marks: object
  canonicalName: string
eventTime: string
createTime: string
severity: string
canonicalName: string
mute: string
findingClass: string
indicator:
  ipAddresses:
    - type: string
  domains:
    - type: string
  signatures:
    - memoryHashSignature:
        binaryFamily: string
        detections:
          - binary: string
            percentPagesMatched: number
      yaraRuleSignature:
        yaraRule: string
      signatureType: string
  uris:
    - type: string
vulnerability:
  cve:
    id: string
    references:
      - source: string
        uri: string
    cvssv3:
      baseScore: number
      attackVector: string
      attackComplexity: string
      privilegesRequired: string
      userInteraction: string
      scope: string
      confidentialityImpact: string
      integrityImpact: string
      availabilityImpact: string
    upstreamFixAvailable: boolean
    impact: string
    exploitationActivity: string
    observedInTheWild: boolean
    zeroDay: boolean
    exploitReleaseDate: string
    firstExploitationDate: string
  offendingPackage:
    packageName: string
    cpeUri: string
    packageType: string
    packageVersion: string
  securityBulletin:
    bulletinId: string
    submissionTime: string
    suggestedUpgradeVersion: string
muteUpdateTime: string
externalSystems: object
mitreAttack:
  primaryTactic: string
  primaryTechniques:
    - type: string
      enumDescriptions: string
      enum: string
  additionalTactics:
    - type: string
      enumDescriptions: string
      enum: string
  additionalTechniques:
    - type: string
      enumDescriptions: string
      enum: string
  version: string
access:
  principalEmail: string
  callerIp: string
  callerIpGeo:
    regionCode: string
  userAgentFamily: string
  userAgent: string
  serviceName: string
  methodName: string
  principalSubject: string
  serviceAccountKeyName: string
  serviceAccountDelegationInfo:
    - principalEmail: string
      principalSubject: string
  userName: string
connections:
  - destinationIp: string
    destinationPort: integer
    sourceIp: string
    sourcePort: integer
    protocol: string
muteInitiator: string
muteInfo:
  staticMute:
    state: string
    applyTime: string
  dynamicMuteRecords:
    - muteConfig: string
      matchTime: string
processes:
  - name: string
    binary:
      path: string
      size: string
      sha256: string
      hashedSize: string
      partiallyHashed: boolean
      contents: string
      diskPath:
        partitionUuid: string
        relativePath: string
    libraries:
      - path: string
        size: string
        sha256: string
        hashedSize: string
        partiallyHashed: boolean
        contents: string
    args:
      - type: string
    argumentsTruncated: boolean
    envVariables:
      - name: string
        val: string
    envVariablesTruncated: boolean
    pid: string
    parentPid: string
contacts: object
compliances:
  - standard: string
    version: string
    ids:
      - type: string
parentDisplayName: string
description: string
exfiltration:
  sources:
    - name: string
      components:
        - type: string
  targets:
    - name: string
      components:
        - type: string
  totalExfiltratedBytes: string
iamBindings:
  - action: string
    role: string
    member: string
nextSteps: string
moduleName: string
containers:
  - name: string
    uri: string
    imageId: string
    labels:
      - name: string
        value: string
    createTime: string
kubernetes:
  pods:
    - ns: string
      name: string
      labels:
        - name: string
          value: string
      containers:
        - name: string
          uri: string
          imageId: string
          labels:
            - name: string
              value: string
          createTime: string
  nodes:
    - name: string
  nodePools:
    - name: string
      nodes:
        - name: string
  roles:
    - kind: string
      ns: string
      name: string
  bindings:
    - ns: string
      name: string
      role:
        kind: string
        ns: string
        name: string
      subjects:
        - kind: string
          ns: string
          name: string
  accessReviews:
    - group: string
      ns: string
      name: string
      resource: string
      subresource: string
      verb: string
      version: string
  objects:
    - group: string
      kind: string
      ns: string
      name: string
      containers:
        - name: string
          uri: string
          imageId: string
          labels:
            - name: string
              value: string
          createTime: string
database:
  name: string
  displayName: string
  userName: string
  query: string
  grantees:
    - type: string
  version: string
attackExposure:
  score: number
  latestCalculationTime: string
  attackExposureResult: string
  state: string
  exposedHighValueResourcesCount: integer
  exposedMediumValueResourcesCount: integer
  exposedLowValueResourcesCount: integer
files:
  - path: string
    size: string
    sha256: string
    hashedSize: string
    partiallyHashed: boolean
    contents: string
cloudDlpInspection:
  inspectJob: string
  infoType: string
  infoTypeCount: string
  fullScan: boolean
cloudDlpDataProfile:
  dataProfile: string
  parentType: string
kernelRootkit:
  name: string
  unexpectedCodeModification: boolean
  unexpectedReadOnlyDataModification: boolean
  unexpectedFtraceHandler: boolean
  unexpectedKprobeHandler: boolean
  unexpectedKernelCodePages: boolean
  unexpectedSystemCallHandler: boolean
  unexpectedInterruptHandler: boolean
  unexpectedProcessesInRunqueue: boolean
orgPolicies:
  - name: string
application:
  baseUri: string
  fullUri: string
backupDisasterRecovery:
  backupTemplate: string
  policies:
    - type: string
  host: string
  applications:
    - type: string
  storagePool: string
  policyOptions:
    - type: string
  profile: string
  appliance: string
  backupType: string
  backupCreateTime: string
securityPosture:
  name: string
  revisionId: string
  postureDeploymentResource: string
  postureDeployment: string
  changedPolicy: string
  policySet: string
  policy: string
  policyDriftDetails:
    - field: string
      expectedValue: string
      detectedValue: string
logEntries:
  - cloudLoggingEntry:
      insertId: string
      logId: string
      resourceContainer: string
      timestamp: string
loadBalancers:
  - name: string
cloudArmor:
  securityPolicy:
    name: string
    type: string
    preview: boolean
  requests:
    ratio: number
    shortTermAllowed: integer
    longTermAllowed: integer
    longTermDenied: integer
  adaptiveProtection:
    confidence: number
  attack:
    volumePps: integer
    volumeBps: integer
    classification: string
  threatVector: string
  duration: string
notebook:
  name: string
  service: string
  lastAuthor: string
  notebookUpdateTime: string
toxicCombination:
  attackExposureScore: number
  relatedFindings:
    - type: string
groupMemberships:
  - groupType: string
    groupId: string
dataAccessEvents:
  - eventId: string
    principalEmail: string
    operation: string
    eventTime: string
dataFlowEvents:
  - eventId: string
    principalEmail: string
    operation: string
    violatedLocation: string
    eventTime: string

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
