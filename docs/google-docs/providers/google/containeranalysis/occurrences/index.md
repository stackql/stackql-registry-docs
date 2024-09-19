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
- name: your_resource_model_name
  props:
    - name: occurrences
      value:
        - - name: noteName
            value: string
          - name: kind
            value: string
          - name: sbomReference
            value:
              - name: signatures
                value:
                  - - name: keyid
                      value: string
                    - name: sig
                      value: string
              - name: payloadType
                value: string
              - name: payload
                value:
                  - name: subject
                    value:
                      - - name: digest
                          value: object
                        - name: name
                          value: string
                  - name: _type
                    value: string
                  - name: predicateType
                    value: string
                  - name: predicate
                    value:
                      - name: digest
                        value: object
                      - name: referrerId
                        value: string
                      - name: mimeType
                        value: string
                      - name: location
                        value: string
          - name: discovery
            value:
              - name: continuousAnalysis
                value: string
              - name: analysisStatus
                value: string
              - name: analysisStatusError
                value:
                  - name: details
                    value:
                      - object
                  - name: message
                    value: string
                  - name: code
                    value: integer
              - name: sbomStatus
                value:
                  - name: sbomState
                    value: string
                  - name: error
                    value: string
              - name: archiveTime
                value: string
              - name: lastScanTime
                value: string
              - name: analysisError
                value:
                  - - name: details
                      value:
                        - object
                    - name: message
                      value: string
                    - name: code
                      value: integer
              - name: analysisCompleted
                value:
                  - name: analysisType
                    value:
                      - string
              - name: cpe
                value: string
          - name: attestation
            value:
              - name: serializedPayload
                value: string
              - name: jwts
                value:
                  - - name: compactJwt
                      value: string
              - name: signatures
                value:
                  - - name: publicKeyId
                      value: string
                    - name: signature
                      value: string
          - name: dsseAttestation
            value:
              - name: statement
                value:
                  - name: predicateType
                    value: string
                  - name: slsaProvenanceZeroTwo
                    value:
                      - name: metadata
                        value:
                          - name: buildInvocationId
                            value: string
                          - name: reproducible
                            value: boolean
                          - name: completeness
                            value:
                              - name: parameters
                                value: boolean
                              - name: environment
                                value: boolean
                              - name: materials
                                value: boolean
                          - name: buildFinishedOn
                            value: string
                          - name: buildStartedOn
                            value: string
                      - name: buildConfig
                        value: object
                      - name: invocation
                        value:
                          - name: parameters
                            value: object
                          - name: configSource
                            value:
                              - name: entryPoint
                                value: string
                              - name: uri
                                value: string
                              - name: digest
                                value: object
                          - name: environment
                            value: object
                      - name: materials
                        value:
                          - - name: digest
                              value: object
                            - name: uri
                              value: string
                      - name: builder
                        value:
                          - name: id
                            value: string
                      - name: buildType
                        value: string
                  - name: _type
                    value: string
                  - name: subject
                    value:
                      - - name: digest
                          value: object
                        - name: name
                          value: string
                  - name: provenance
                    value:
                      - name: builderConfig
                        value:
                          - name: id
                            value: string
                      - name: recipe
                        value:
                          - name: environment
                            value:
                              - object
                          - name: type
                            value: string
                          - name: arguments
                            value:
                              - object
                          - name: definedInMaterial
                            value: string
                          - name: entryPoint
                            value: string
                      - name: metadata
                        value:
                          - name: buildStartedOn
                            value: string
                          - name: reproducible
                            value: boolean
                          - name: buildInvocationId
                            value: string
                          - name: completeness
                            value:
                              - name: arguments
                                value: boolean
                              - name: environment
                                value: boolean
                              - name: materials
                                value: boolean
                          - name: buildFinishedOn
                            value: string
                      - name: materials
                        value:
                          - string
                  - name: slsaProvenance
                    value:
                      - name: builder
                        value:
                          - name: id
                            value: string
                      - name: materials
                        value:
                          - - name: digest
                              value: object
                            - name: uri
                              value: string
                      - name: recipe
                        value:
                          - name: arguments
                            value: object
                          - name: definedInMaterial
                            value: string
                          - name: environment
                            value: object
                          - name: type
                            value: string
                          - name: entryPoint
                            value: string
                      - name: metadata
                        value:
                          - name: completeness
                            value:
                              - name: arguments
                                value: boolean
                              - name: materials
                                value: boolean
                              - name: environment
                                value: boolean
                          - name: reproducible
                            value: boolean
                          - name: buildFinishedOn
                            value: string
                          - name: buildStartedOn
                            value: string
                          - name: buildInvocationId
                            value: string
              - name: envelope
                value:
                  - name: payloadType
                    value: string
                  - name: signatures
                    value:
                      - - name: keyid
                          value: string
                        - name: sig
                          value: string
                  - name: payload
                    value: string
          - name: vulnerability
            value:
              - name: cvssVersion
                value: string
              - name: severity
                value: string
              - name: shortDescription
                value: string
              - name: relatedUrls
                value:
                  - - name: label
                      value: string
                    - name: url
                      value: string
              - name: vexAssessment
                value:
                  - name: impacts
                    value:
                      - string
                  - name: relatedUris
                    value:
                      - - name: label
                          value: string
                        - name: url
                          value: string
                  - name: remediations
                    value:
                      - - name: remediationUri
                          value:
                            - name: label
                              value: string
                            - name: url
                              value: string
                        - name: remediationType
                          value: string
                        - name: details
                          value: string
                  - name: noteName
                    value: string
                  - name: justification
                    value:
                      - name: justificationType
                        value: string
                      - name: details
                        value: string
                  - name: vulnerabilityId
                    value: string
                  - name: cve
                    value: string
                  - name: state
                    value: string
              - name: type
                value: string
              - name: packageIssue
                value:
                  - - name: fileLocation
                      value:
                        - - name: filePath
                            value: string
                    - name: affectedCpeUri
                      value: string
                    - name: packageType
                      value: string
                    - name: fixedVersion
                      value:
                        - name: inclusive
                          value: boolean
                        - name: revision
                          value: string
                        - name: fullName
                          value: string
                        - name: epoch
                          value: integer
                        - name: name
                          value: string
                        - name: kind
                          value: string
                    - name: fixAvailable
                      value: boolean
                    - name: fixedCpeUri
                      value: string
                    - name: effectiveSeverity
                      value: string
                    - name: affectedPackage
                      value: string
                    - name: fixedPackage
                      value: string
              - name: extraDetails
                value: string
              - name: cvssV2
                value:
                  - name: attackComplexity
                    value: string
                  - name: exploitabilityScore
                    value: number
                  - name: impactScore
                    value: number
                  - name: availabilityImpact
                    value: string
                  - name: baseScore
                    value: number
                  - name: attackVector
                    value: string
                  - name: scope
                    value: string
                  - name: integrityImpact
                    value: string
                  - name: confidentialityImpact
                    value: string
                  - name: privilegesRequired
                    value: string
                  - name: authentication
                    value: string
                  - name: userInteraction
                    value: string
              - name: effectiveSeverity
                value: string
              - name: longDescription
                value: string
              - name: fixAvailable
                value: boolean
              - name: cvssScore
                value: number
          - name: image
            value:
              - name: baseResourceUrl
                value: string
              - name: fingerprint
                value:
                  - name: v2Blob
                    value:
                      - string
                  - name: v2Name
                    value: string
                  - name: v1Name
                    value: string
              - name: layerInfo
                value:
                  - - name: arguments
                      value: string
                    - name: directive
                      value: string
              - name: distance
                value: integer
          - name: name
            value: string
          - name: createTime
            value: string
          - name: compliance
            value:
              - name: version
                value:
                  - name: cpeUri
                    value: string
                  - name: benchmarkDocument
                    value: string
                  - name: version
                    value: string
              - name: nonComplianceReason
                value: string
              - name: nonCompliantFiles
                value:
                  - - name: reason
                      value: string
                    - name: path
                      value: string
                    - name: displayCommand
                      value: string
          - name: upgrade
            value:
              - name: package
                value: string
              - name: windowsUpdate
                value:
                  - name: description
                    value: string
                  - name: categories
                    value:
                      - - name: categoryId
                          value: string
                        - name: name
                          value: string
                  - name: title
                    value: string
                  - name: identity
                    value:
                      - name: updateId
                        value: string
                      - name: revision
                        value: integer
                  - name: supportUrl
                    value: string
                  - name: lastPublishedTimestamp
                    value: string
                  - name: kbArticleIds
                    value:
                      - string
              - name: distribution
                value:
                  - name: cpeUri
                    value: string
                  - name: classification
                    value: string
                  - name: severity
                    value: string
                  - name: cve
                    value:
                      - string
          - name: package
            value:
              - name: architecture
                value: string
              - name: packageType
                value: string
              - name: license
                value:
                  - name: comments
                    value: string
                  - name: expression
                    value: string
              - name: name
                value: string
              - name: cpeUri
                value: string
              - name: location
                value:
                  - - name: path
                      value: string
                    - name: cpeUri
                      value: string
          - name: deployment
            value:
              - name: undeployTime
                value: string
              - name: config
                value: string
              - name: address
                value: string
              - name: userEmail
                value: string
              - name: platform
                value: string
              - name: resourceUri
                value:
                  - string
              - name: deployTime
                value: string
          - name: updateTime
            value: string
          - name: build
            value:
              - name: inTotoSlsaProvenanceV1
                value:
                  - name: subject
                    value:
                      - - name: digest
                          value: object
                        - name: name
                          value: string
                  - name: predicate
                    value:
                      - name: runDetails
                        value:
                          - name: builder
                            value:
                              - name: builderDependencies
                                value:
                                  - - name: uri
                                      value: string
                                    - name: downloadLocation
                                      value: string
                                    - name: content
                                      value: string
                                    - name: mediaType
                                      value: string
                                    - name: name
                                      value: string
                                    - name: digest
                                      value: object
                                    - name: annotations
                                      value: object
                              - name: version
                                value: object
                              - name: id
                                value: string
                          - name: metadata
                            value:
                              - name: finishedOn
                                value: string
                              - name: startedOn
                                value: string
                              - name: invocationId
                                value: string
                          - name: byproducts
                            value:
                              - - name: uri
                                  value: string
                                - name: downloadLocation
                                  value: string
                                - name: content
                                  value: string
                                - name: mediaType
                                  value: string
                                - name: name
                                  value: string
                                - name: digest
                                  value: object
                                - name: annotations
                                  value: object
                      - name: buildDefinition
                        value:
                          - name: buildType
                            value: string
                          - name: externalParameters
                            value: object
                          - name: resolvedDependencies
                            value:
                              - - name: uri
                                  value: string
                                - name: downloadLocation
                                  value: string
                                - name: content
                                  value: string
                                - name: mediaType
                                  value: string
                                - name: name
                                  value: string
                                - name: digest
                                  value: object
                                - name: annotations
                                  value: object
                          - name: internalParameters
                            value: object
                  - name: _type
                    value: string
                  - name: predicateType
                    value: string
              - name: provenance
                value:
                  - name: createTime
                    value: string
                  - name: projectId
                    value: string
                  - name: commands
                    value:
                      - - name: dir
                          value: string
                        - name: id
                          value: string
                        - name: env
                          value:
                            - string
                        - name: args
                          value:
                            - string
                        - name: waitFor
                          value:
                            - string
                        - name: name
                          value: string
                  - name: buildOptions
                    value: object
                  - name: builtArtifacts
                    value:
                      - - name: checksum
                          value: string
                        - name: id
                          value: string
                        - name: names
                          value:
                            - string
                  - name: id
                    value: string
                  - name: startTime
                    value: string
                  - name: endTime
                    value: string
                  - name: creator
                    value: string
                  - name: logsUri
                    value: string
                  - name: builderVersion
                    value: string
                  - name: triggerId
                    value: string
                  - name: sourceProvenance
                    value:
                      - name: additionalContexts
                        value:
                          - - name: labels
                              value: object
                            - name: cloudRepo
                              value:
                                - name: revisionId
                                  value: string
                                - name: repoId
                                  value:
                                    - name: uid
                                      value: string
                                    - name: projectRepoId
                                      value:
                                        - name: repoName
                                          value: string
                                        - name: projectId
                                          value: string
                                - name: aliasContext
                                  value:
                                    - name: kind
                                      value: string
                                    - name: name
                                      value: string
                            - name: git
                              value:
                                - name: revisionId
                                  value: string
                                - name: url
                                  value: string
                            - name: gerrit
                              value:
                                - name: gerritProject
                                  value: string
                                - name: revisionId
                                  value: string
                                - name: hostUri
                                  value: string
                      - name: artifactStorageSourceUri
                        value: string
                      - name: fileHashes
                        value: object
                      - name: context
                        value:
                          - name: labels
                            value: object
              - name: provenanceBytes
                value: string
          - name: resourceUri
            value: string
          - name: remediation
            value: string

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
