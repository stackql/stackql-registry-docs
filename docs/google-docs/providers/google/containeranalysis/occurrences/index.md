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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>occurrences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.containeranalysis.occurrences</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of the occurrence in the form of `projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]`. |
| `deployment` | `object` | The period during which some deployable was active in a runtime. |
| `discovery` | `object` | Provides information about the analysis status of a discovered resource. |
| `resourceUri` | `string` | Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, `https://gcr.io/project/image@sha256:123abc` for a Docker image. |
| `noteName` | `string` | Required. Immutable. The analysis note associated with this occurrence, in the form of `projects/[PROVIDER_ID]/notes/[NOTE_ID]`. This field can be used as a filter in list requests. |
| `upgrade` | `object` | An Upgrade Occurrence represents that a specific resource_url could install a specific upgrade. This presence is supplied via local sources (i.e. it is present in the mirror and the running system has noticed its availability). For Windows, both distribution and windows_update contain information for the Windows update. |
| `build` | `object` | Details of a build occurrence. |
| `remediation` | `string` | A description of actions that can be taken to remedy the note. |
| `updateTime` | `string` | Output only. The time this occurrence was last updated. |
| `image` | `object` | Details of the derived image portion of the DockerImage relationship. This image would be produced from a Dockerfile with FROM . |
| `createTime` | `string` | Output only. The time this occurrence was created. |
| `sbomReference` | `object` | The occurrence representing an SBOM reference as applied to a specific resource. The occurrence follows the DSSE specification. See https://github.com/secure-systems-lab/dsse/blob/master/envelope.md for more details. |
| `package` | `object` | Details on how a particular software package was installed on a system. |
| `dsseAttestation` | `object` | Deprecated. Prefer to use a regular Occurrence, and populate the Envelope at the top level of the Occurrence. |
| `kind` | `string` | Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests. |
| `attestation` | `object` | Occurrence that represents a single "attestation". The authenticity of an attestation can be verified using the attached signature. If the verifier trusts the public key of the signer, then verifying the signature is sufficient to establish trust. In this circumstance, the authority to which this attestation is attached is primarily useful for lookup (how to find this attestation if you already know the authority and artifact to be verified) and intent (for which authority this attestation was intended to sign. |
| `compliance` | `object` | An indication that the compliance checks in the associated ComplianceNote were not satisfied for particular resources or a specified reason. |
| `vulnerability` | `object` | An occurrence of a severity vulnerability on a resource. |
| `envelope` | `object` | MUST match https://github.com/secure-systems-lab/dsse/blob/master/envelope.proto. An authenticated message of arbitrary type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_notes_occurrences_list` | `SELECT` | `notesId, projectsId` | Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note. |
| `projects_occurrences_get` | `SELECT` | `occurrencesId, projectsId` | Gets the specified occurrence. |
| `projects_occurrences_list` | `SELECT` | `projectsId` | Lists occurrences for the specified project. |
| `projects_occurrences_create` | `INSERT` | `projectsId` | Creates a new occurrence. |
| `projects_occurrences_delete` | `DELETE` | `occurrencesId, projectsId` | Deletes the specified occurrence. For example, use this method to delete an occurrence when the occurrence is no longer applicable for the given resource. |
| `_projects_notes_occurrences_list` | `EXEC` | `notesId, projectsId` | Lists occurrences referencing the specified note. Provider projects can use this method to get all occurrences across consumer projects referencing the specified note. |
| `_projects_occurrences_list` | `EXEC` | `projectsId` | Lists occurrences for the specified project. |
| `projects_occurrences_batch_create` | `EXEC` | `projectsId` | Creates new occurrences in batch. |
| `projects_occurrences_patch` | `EXEC` | `occurrencesId, projectsId` | Updates the specified occurrence. |
