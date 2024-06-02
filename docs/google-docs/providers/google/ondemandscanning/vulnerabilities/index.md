---
title: vulnerabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - vulnerabilities
  - ondemandscanning
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vulnerabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="ondemandscanning.vulnerabilities" /></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, scansId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, scansId" /> |
