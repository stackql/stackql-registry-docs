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
  - resourceUri: string
    discovery:
      sbomStatus:
        error: string
        sbomState: string
      continuousAnalysis: string
      cpe: string
      analysisCompleted:
        analysisType:
          - type: string
      analysisStatusError:
        details:
          - additionalProperties: any
            type: string
        code: integer
        message: string
      analysisError:
        - details:
            - additionalProperties: any
              type: string
          code: integer
          message: string
      archiveTime: string
      analysisStatus: string
      lastScanTime: string
    image:
      distance: integer
      fingerprint:
        v2Name: string
        v1Name: string
        v2Blob:
          - type: string
      baseResourceUrl: string
      layerInfo:
        - directive: string
          arguments: string
    vulnerability:
      vexAssessment:
        state: string
        cve: string
        relatedUris:
          - url: string
            label: string
        justification:
          justificationType: string
          details: string
        impacts:
          - type: string
        remediations:
          - remediationType: string
            details: string
            remediationUri:
              url: string
              label: string
        noteName: string
        vulnerabilityId: string
      effectiveSeverity: string
      packageIssue:
        - fixedVersion:
            kind: string
            fullName: string
            revision: string
            name: string
            inclusive: boolean
            epoch: integer
          fileLocation:
            - filePath: string
          fixedCpeUri: string
          fixAvailable: boolean
          effectiveSeverity: string
          fixedPackage: string
          affectedCpeUri: string
          packageType: string
          affectedPackage: string
      fixAvailable: boolean
      cvssScore: number
      type: string
      relatedUrls:
        - url: string
          label: string
      cvssVersion: string
      severity: string
      shortDescription: string
      longDescription: string
      cvssV2:
        baseScore: number
        authentication: string
        attackComplexity: string
        scope: string
        attackVector: string
        impactScore: number
        availabilityImpact: string
        privilegesRequired: string
        userInteraction: string
        exploitabilityScore: number
        confidentialityImpact: string
        integrityImpact: string
      extraDetails: string
    package:
      location:
        - cpeUri: string
          path: string
      packageType: string
      architecture: string
      cpeUri: string
      name: string
      license:
        comments: string
        expression: string
    attestation:
      jwts:
        - compactJwt: string
      serializedPayload: string
      signatures:
        - signature: string
          publicKeyId: string
    build:
      inTotoSlsaProvenanceV1:
        _type: string
        predicate:
          buildDefinition:
            buildType: string
            internalParameters: object
            externalParameters: object
            resolvedDependencies:
              - annotations: object
                mediaType: string
                content: string
                downloadLocation: string
                digest: object
                name: string
                uri: string
          runDetails:
            byproducts:
              - annotations: object
                mediaType: string
                content: string
                downloadLocation: string
                digest: object
                name: string
                uri: string
            builder:
              version: object
              id: string
              builderDependencies:
                - annotations: object
                  mediaType: string
                  content: string
                  downloadLocation: string
                  digest: object
                  name: string
                  uri: string
            metadata:
              invocationId: string
              finishedOn: string
              startedOn: string
        predicateType: string
        subject:
          - digest: object
            name: string
      intotoStatement:
        predicateType: string
        subject:
          - digest: object
            name: string
        _type: string
        slsaProvenanceZeroTwo:
          builder:
            id: string
          buildType: string
          invocation:
            environment: object
            configSource:
              uri: string
              entryPoint: string
              digest: object
            parameters: object
          buildConfig: object
          materials:
            - uri: string
              digest: object
          metadata:
            buildInvocationId: string
            reproducible: boolean
            buildFinishedOn: string
            buildStartedOn: string
            completeness:
              parameters: boolean
              materials: boolean
              environment: boolean
        slsaProvenance:
          metadata:
            buildInvocationId: string
            completeness:
              arguments: boolean
              materials: boolean
              environment: boolean
            reproducible: boolean
            buildFinishedOn: string
            buildStartedOn: string
          materials:
            - uri: string
              digest: object
          recipe:
            type: string
            arguments: object
            definedInMaterial: string
            entryPoint: string
            environment: object
          builder:
            id: string
        provenance:
          materials:
            - type: string
          metadata:
            completeness:
              arguments: boolean
              materials: boolean
              environment: boolean
            buildStartedOn: string
            buildInvocationId: string
            buildFinishedOn: string
            reproducible: boolean
          builderConfig:
            id: string
          recipe:
            entryPoint: string
            definedInMaterial: string
            environment:
              - type: string
                additionalProperties: any
            type: string
            arguments:
              - type: string
                additionalProperties: any
      provenance:
        createTime: string
        endTime: string
        creator: string
        id: string
        projectId: string
        commands:
          - id: string
            args:
              - type: string
            env:
              - type: string
            dir: string
            name: string
            waitFor:
              - type: string
        startTime: string
        builderVersion: string
        logsUri: string
        triggerId: string
        buildOptions: object
        builtArtifacts:
          - names:
              - type: string
            id: string
            checksum: string
        sourceProvenance:
          additionalContexts:
            - gerrit:
                gerritProject: string
                aliasContext:
                  name: string
                  kind: string
                hostUri: string
                revisionId: string
              cloudRepo:
                repoId:
                  projectRepoId:
                    repoName: string
                    projectId: string
                  uid: string
                revisionId: string
              labels: object
              git:
                revisionId: string
                url: string
          context:
            labels: object
          fileHashes: object
          artifactStorageSourceUri: string
      provenanceBytes: string
    kind: string
    updateTime: string
    createTime: string
    compliance:
      nonComplianceReason: string
      version:
        cpeUri: string
        benchmarkDocument: string
        version: string
      nonCompliantFiles:
        - reason: string
          path: string
          displayCommand: string
    remediation: string
    sbomReference:
      payloadType: string
      payload:
        predicate:
          mimeType: string
          digest: object
          referrerId: string
          location: string
        subject:
          - digest: object
            name: string
        predicateType: string
        _type: string
      signatures:
        - keyid: string
          sig: string
    name: string
    envelope:
      signatures:
        - keyid: string
          sig: string
      payload: string
      payloadType: string
    upgrade:
      windowsUpdate:
        title: string
        categories:
          - name: string
            categoryId: string
        identity:
          revision: integer
          updateId: string
        description: string
        kbArticleIds:
          - type: string
        lastPublishedTimestamp: string
        supportUrl: string
      package: string
      distribution:
        cpeUri: string
        classification: string
        cve:
          - type: string
        severity: string
    dsseAttestation: {}
    deployment:
      config: string
      platform: string
      deployTime: string
      undeployTime: string
      address: string
      resourceUri:
        - type: string
      userEmail: string
    noteName: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>occurrences</code> resource.

```sql
/*+ update */
UPDATE google.containeranalysis.occurrences
SET 
resourceUri = '{{ resourceUri }}',
discovery = '{{ discovery }}',
image = '{{ image }}',
vulnerability = '{{ vulnerability }}',
package = '{{ package }}',
attestation = '{{ attestation }}',
build = '{{ build }}',
compliance = '{{ compliance }}',
remediation = '{{ remediation }}',
sbomReference = '{{ sbomReference }}',
name = '{{ name }}',
envelope = '{{ envelope }}',
upgrade = '{{ upgrade }}',
dsseAttestation = '{{ dsseAttestation }}',
deployment = '{{ deployment }}',
noteName = '{{ noteName }}'
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
