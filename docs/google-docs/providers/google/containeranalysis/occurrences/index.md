---
title: occurrences
hide_title: false
hide_table_of_contents: false
keywords:
  - occurrences
  - containeranalysis
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

Creates, updates, deletes, gets or lists a <code>occurrences</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>occurrences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.containeranalysis.occurrences" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`. |
| <CopyableCode code="attestation" /> | `object` | Occurrence that represents a single "attestation". The authenticity of an attestation can be verified using the attached signature. If the verifier trusts the public key of the signer, then verifying the signature is sufficient to establish trust. In this circumstance, the authority to which this attestation is attached is primarily useful for lookup (how to find this attestation if you already know the authority and artifact to be verified) and intent (for which authority this attestation was intended to sign. |
| <CopyableCode code="build" /> | `object` | Details of a build occurrence. |
| <CopyableCode code="compliance" /> | `object` | An indication that the compliance checks in the associated ComplianceNote were not satisfied for particular resources or a specified reason. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time this occurrence was created. |
| <CopyableCode code="deployment" /> | `object` | The period during which some deployable was active in a runtime. |
| <CopyableCode code="discovery" /> | `object` | Provides information about the analysis status of a discovered resource. |
| <CopyableCode code="dsseAttestation" /> | `object` | Deprecated. Prefer to use a regular Occurrence, and populate the Envelope at the top level of the Occurrence. |
| <CopyableCode code="envelope" /> | `object` | MUST match https://github.com/secure-systems-lab/dsse/blob/master/envelope.proto. An authenticated message of arbitrary type. |
| <CopyableCode code="image" /> | `object` | Details of the derived image portion of the DockerImage relationship. This image would be produced from a Dockerfile with FROM . |
| <CopyableCode code="kind" /> | `string` | Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests. |
| <CopyableCode code="noteName" /> | `string` | Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests. |
| <CopyableCode code="package" /> | `object` | Details on how a particular software package was installed on a system. |
| <CopyableCode code="remediation" /> | `string` | A description of actions that can be taken to remedy the note. |
| <CopyableCode code="resourceUri" /> | `string` | Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, `https://gcr.io/project/image@sha256:123abc` for a Docker image. |
| <CopyableCode code="sbomReference" /> | `object` | The occurrence representing an SBOM reference as applied to a specific resource. The occurrence follows the DSSE specification. See https://github.com/secure-systems-lab/dsse/blob/master/envelope.md for more details. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time this occurrence was last updated. |
| <CopyableCode code="upgrade" /> | `object` | An Upgrade Occurrence represents that a specific resource_url could install a specific upgrade. This presence is supplied via local sources (i.e. it is present in the mirror and the running system has noticed its availability). For Windows, both distribution and windows_update contain information for the Windows update. |
| <CopyableCode code="vulnerability" /> | `object` | An occurrence of a severity vulnerability on a resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_notes_occurrences_list" /> | `SELECT` | <CopyableCode code="locationsId, notesId, projectsId" /> | Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note. |
| <CopyableCode code="projects_locations_occurrences_get" /> | `SELECT` | <CopyableCode code="locationsId, occurrencesId, projectsId" /> | Gets the specified occurrence. |
| <CopyableCode code="projects_locations_occurrences_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists occurrences for the specified project. |
| <CopyableCode code="projects_notes_occurrences_list" /> | `SELECT` | <CopyableCode code="notesId, projectsId" /> | Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note. |
| <CopyableCode code="projects_occurrences_get" /> | `SELECT` | <CopyableCode code="occurrencesId, projectsId" /> | Gets the specified occurrence. |
| <CopyableCode code="projects_occurrences_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists occurrences for the specified project. |
| <CopyableCode code="projects_locations_occurrences_batch_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates new occurrences in batch. |
| <CopyableCode code="projects_locations_occurrences_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new occurrence. |
| <CopyableCode code="projects_occurrences_batch_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates new occurrences in batch. |
| <CopyableCode code="projects_occurrences_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new occurrence. |
| <CopyableCode code="projects_locations_occurrences_delete" /> | `DELETE` | <CopyableCode code="locationsId, occurrencesId, projectsId" /> | Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource. |
| <CopyableCode code="projects_occurrences_delete" /> | `DELETE` | <CopyableCode code="occurrencesId, projectsId" /> | Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource. |
| <CopyableCode code="projects_locations_occurrences_patch" /> | `UPDATE` | <CopyableCode code="locationsId, occurrencesId, projectsId" /> | Updates the specified occurrence. |
| <CopyableCode code="projects_occurrences_patch" /> | `UPDATE` | <CopyableCode code="occurrencesId, projectsId" /> | Updates the specified occurrence. |

## `SELECT` examples

Lists occurrences for the specified project.

```sql
SELECT
name,
attestation,
build,
compliance,
createTime,
deployment,
discovery,
dsseAttestation,
envelope,
image,
kind,
noteName,
package,
remediation,
resourceUri,
sbomReference,
updateTime,
upgrade,
vulnerability
FROM google.containeranalysis.occurrences
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>occurrences</code> resource.

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
INSERT INTO google.containeranalysis.occurrences (
projectsId,
occurrences
)
SELECT 
'{{ projectsId }}',
'{{ occurrences }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
occurrences:
  - noteName: string
    kind: string
    sbomReference:
      signatures:
        - keyid: string
          sig: string
      payloadType: string
      payload:
        subject:
          - digest: object
            name: string
        _type: string
        predicateType: string
        predicate:
          digest: object
          referrerId: string
          mimeType: string
          location: string
    discovery:
      continuousAnalysis: string
      analysisStatus: string
      analysisStatusError:
        details:
          - type: string
            additionalProperties: any
        message: string
        code: integer
      sbomStatus:
        sbomState: string
        error: string
      archiveTime: string
      lastScanTime: string
      analysisError:
        - details:
            - type: string
              additionalProperties: any
          message: string
          code: integer
      analysisCompleted:
        analysisType:
          - type: string
      cpe: string
    attestation:
      serializedPayload: string
      jwts:
        - compactJwt: string
      signatures:
        - publicKeyId: string
          signature: string
    dsseAttestation:
      statement:
        predicateType: string
        slsaProvenanceZeroTwo:
          metadata:
            buildInvocationId: string
            reproducible: boolean
            completeness:
              parameters: boolean
              environment: boolean
              materials: boolean
            buildFinishedOn: string
            buildStartedOn: string
          buildConfig: object
          invocation:
            parameters: object
            configSource:
              entryPoint: string
              uri: string
              digest: object
            environment: object
          materials:
            - digest: object
              uri: string
          builder:
            id: string
          buildType: string
        _type: string
        subject:
          - digest: object
            name: string
        provenance:
          builderConfig:
            id: string
          recipe:
            environment:
              - additionalProperties: any
                type: string
            type: string
            arguments:
              - additionalProperties: any
                type: string
            definedInMaterial: string
            entryPoint: string
          metadata:
            buildStartedOn: string
            reproducible: boolean
            buildInvocationId: string
            completeness:
              arguments: boolean
              environment: boolean
              materials: boolean
            buildFinishedOn: string
          materials:
            - type: string
        slsaProvenance:
          builder:
            id: string
          materials:
            - digest: object
              uri: string
          recipe:
            arguments: object
            definedInMaterial: string
            environment: object
            type: string
            entryPoint: string
          metadata:
            completeness:
              arguments: boolean
              materials: boolean
              environment: boolean
            reproducible: boolean
            buildFinishedOn: string
            buildStartedOn: string
            buildInvocationId: string
      envelope:
        payloadType: string
        signatures:
          - keyid: string
            sig: string
        payload: string
    vulnerability:
      cvssVersion: string
      severity: string
      shortDescription: string
      relatedUrls:
        - label: string
          url: string
      vexAssessment:
        impacts:
          - type: string
        relatedUris:
          - label: string
            url: string
        remediations:
          - remediationUri:
              label: string
              url: string
            remediationType: string
            details: string
        noteName: string
        justification:
          justificationType: string
          details: string
        vulnerabilityId: string
        cve: string
        state: string
      type: string
      packageIssue:
        - fileLocation:
            - filePath: string
          affectedCpeUri: string
          packageType: string
          fixedVersion:
            inclusive: boolean
            revision: string
            fullName: string
            epoch: integer
            name: string
            kind: string
          fixAvailable: boolean
          fixedCpeUri: string
          effectiveSeverity: string
          affectedPackage: string
          fixedPackage: string
      extraDetails: string
      cvssV2:
        attackComplexity: string
        exploitabilityScore: number
        impactScore: number
        availabilityImpact: string
        baseScore: number
        attackVector: string
        scope: string
        integrityImpact: string
        confidentialityImpact: string
        privilegesRequired: string
        authentication: string
        userInteraction: string
      effectiveSeverity: string
      longDescription: string
      fixAvailable: boolean
      cvssScore: number
    image:
      baseResourceUrl: string
      fingerprint:
        v2Blob:
          - type: string
        v2Name: string
        v1Name: string
      layerInfo:
        - arguments: string
          directive: string
      distance: integer
    name: string
    createTime: string
    compliance:
      version:
        cpeUri: string
        benchmarkDocument: string
        version: string
      nonComplianceReason: string
      nonCompliantFiles:
        - reason: string
          path: string
          displayCommand: string
    upgrade:
      package: string
      windowsUpdate:
        description: string
        categories:
          - categoryId: string
            name: string
        title: string
        identity:
          updateId: string
          revision: integer
        supportUrl: string
        lastPublishedTimestamp: string
        kbArticleIds:
          - type: string
      distribution:
        cpeUri: string
        classification: string
        severity: string
        cve:
          - type: string
    package:
      architecture: string
      packageType: string
      license:
        comments: string
        expression: string
      name: string
      cpeUri: string
      location:
        - path: string
          cpeUri: string
    deployment:
      undeployTime: string
      config: string
      address: string
      userEmail: string
      platform: string
      resourceUri:
        - type: string
      deployTime: string
    updateTime: string
    build:
      inTotoSlsaProvenanceV1:
        subject:
          - digest: object
            name: string
        predicate:
          runDetails:
            builder:
              builderDependencies:
                - uri: string
                  downloadLocation: string
                  content: string
                  mediaType: string
                  name: string
                  digest: object
                  annotations: object
              version: object
              id: string
            metadata:
              finishedOn: string
              startedOn: string
              invocationId: string
            byproducts:
              - uri: string
                downloadLocation: string
                content: string
                mediaType: string
                name: string
                digest: object
                annotations: object
          buildDefinition:
            buildType: string
            externalParameters: object
            resolvedDependencies:
              - uri: string
                downloadLocation: string
                content: string
                mediaType: string
                name: string
                digest: object
                annotations: object
            internalParameters: object
        _type: string
        predicateType: string
      provenance:
        createTime: string
        projectId: string
        commands:
          - dir: string
            id: string
            env:
              - type: string
            args:
              - type: string
            waitFor:
              - type: string
            name: string
        buildOptions: object
        builtArtifacts:
          - checksum: string
            id: string
            names:
              - type: string
        id: string
        startTime: string
        endTime: string
        creator: string
        logsUri: string
        builderVersion: string
        triggerId: string
        sourceProvenance:
          additionalContexts:
            - labels: object
              cloudRepo:
                revisionId: string
                repoId:
                  uid: string
                  projectRepoId:
                    repoName: string
                    projectId: string
                aliasContext:
                  kind: string
                  name: string
              git:
                revisionId: string
                url: string
              gerrit:
                gerritProject: string
                revisionId: string
                hostUri: string
          artifactStorageSourceUri: string
          fileHashes: object
          context:
            labels: object
      provenanceBytes: string
    resourceUri: string
    remediation: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>occurrences</code> resource.

```sql
/*+ update */
UPDATE google.containeranalysis.occurrences
SET 
noteName = '{{ noteName }}',
sbomReference = '{{ sbomReference }}',
discovery = '{{ discovery }}',
attestation = '{{ attestation }}',
dsseAttestation = '{{ dsseAttestation }}',
vulnerability = '{{ vulnerability }}',
image = '{{ image }}',
envelope = '{{ envelope }}',
name = '{{ name }}',
compliance = '{{ compliance }}',
upgrade = '{{ upgrade }}',
package = '{{ package }}',
deployment = '{{ deployment }}',
build = '{{ build }}',
resourceUri = '{{ resourceUri }}',
remediation = '{{ remediation }}'
WHERE 
occurrencesId = '{{ occurrencesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>occurrences</code> resource.

```sql
/*+ delete */
DELETE FROM google.containeranalysis.occurrences
WHERE occurrencesId = '{{ occurrencesId }}'
AND projectsId = '{{ projectsId }}';
```
