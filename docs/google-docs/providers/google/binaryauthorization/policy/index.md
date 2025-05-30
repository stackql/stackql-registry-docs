---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
  - binaryauthorization
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

Creates, updates, deletes, gets or lists a <code>policy</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.binaryauthorization.policy" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name, in the format `projects/*/policy`. There is at most one policy per project. |
| <CopyableCode code="description" /> | `string` | Optional. A descriptive comment. |
| <CopyableCode code="admissionWhitelistPatterns" /> | `array` | Optional. Admission policy allowlisting. A matching admission request will always be permitted. This feature is typically used to exclude Google or third-party infrastructure images from Binary Authorization policies. |
| <CopyableCode code="clusterAdmissionRules" /> | `object` | Optional. Per-cluster admission rules. Cluster spec format: `location.clusterId`. There can be at most one admission rule per cluster spec. A `location` is either a compute zone (e.g. us-central1-a) or a region (e.g. us-central1). For `clusterId` syntax restrictions see https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters. |
| <CopyableCode code="defaultAdmissionRule" /> | `object` | An admission rule specifies either that all container images used in a pod creation request must be attested to by one or more attestors, that all pod creations will be allowed, or that all pod creations will be denied. Images matching an admission allowlist pattern are exempted from admission rules and will never block a pod creation. |
| <CopyableCode code="etag" /> | `string` | Optional. A checksum, returned by the server, that can be sent on update requests to ensure the policy has an up-to-date value before attempting to update it. See https://google.aip.dev/154. |
| <CopyableCode code="globalPolicyEvaluationMode" /> | `string` | Optional. Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not covered by the global policy will be subject to the project admission policy. This setting has no effect when specified inside a global admission policy. |
| <CopyableCode code="istioServiceIdentityAdmissionRules" /> | `object` | Optional. Per-istio-service-identity admission rules. Istio service identity spec format: `spiffe:///ns//sa/` or `/ns//sa/` e.g. `spiffe://example.com/ns/test-ns/sa/default` |
| <CopyableCode code="kubernetesNamespaceAdmissionRules" /> | `object` | Optional. Per-kubernetes-namespace admission rules. K8s namespace spec format: `[a-z.-]+`, e.g. `some-namespace` |
| <CopyableCode code="kubernetesServiceAccountAdmissionRules" /> | `object` | Optional. Per-kubernetes-service-account admission rules. Service account spec format: `namespace:serviceaccount`. e.g. `test-ns:default` |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the policy was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_policy" /> | `SELECT` | <CopyableCode code="projectsId" /> | A policy specifies the attestors that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy. Gets the policy for this project. Returns a default policy if the project does not have one. |
| <CopyableCode code="update_policy" /> | `REPLACE` | <CopyableCode code="projectsId" /> | Creates or updates a project's policy, and returns a copy of the new policy. A policy is always updated as a whole, to avoid race conditions with concurrent policy enforcement (or management!) requests. Returns `NOT_FOUND` if the project does not exist, `INVALID_ARGUMENT` if the request is malformed. |

## `SELECT` examples

A policy specifies the attestors that must attest to a container image, before the project is allowed to deploy that image. There is at most one policy per project. All image admission requests are permitted if a project has no policy. Gets the policy for this project. Returns a default policy if the project does not have one.

```sql
SELECT
name,
description,
admissionWhitelistPatterns,
clusterAdmissionRules,
defaultAdmissionRule,
etag,
globalPolicyEvaluationMode,
istioServiceIdentityAdmissionRules,
kubernetesNamespaceAdmissionRules,
kubernetesServiceAccountAdmissionRules,
updateTime
FROM google.binaryauthorization.policy
WHERE projectsId = '{{ projectsId }}';
```

## `REPLACE` example

Replaces all fields in the specified <code>policy</code> resource.

```sql
/*+ update */
REPLACE google.binaryauthorization.policy
SET 
description = '{{ description }}',
globalPolicyEvaluationMode = '{{ globalPolicyEvaluationMode }}',
admissionWhitelistPatterns = '{{ admissionWhitelistPatterns }}',
clusterAdmissionRules = '{{ clusterAdmissionRules }}',
kubernetesNamespaceAdmissionRules = '{{ kubernetesNamespaceAdmissionRules }}',
kubernetesServiceAccountAdmissionRules = '{{ kubernetesServiceAccountAdmissionRules }}',
istioServiceIdentityAdmissionRules = '{{ istioServiceIdentityAdmissionRules }}',
defaultAdmissionRule = '{{ defaultAdmissionRule }}',
etag = '{{ etag }}'
WHERE 
projectsId = '{{ projectsId }}';
```
