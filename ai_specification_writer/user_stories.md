# User Stories

### User Story 1
As a spec author, I want to start a new spec from a guided template so that I can capture the required sections without missing anything.

**Acceptance Criteria**:
- User can create a new spec and is prompted for the core sections (problem, scope, constraints, non-goals).  
- System prevents publishing/exporting until required sections are completed.  
- User can save progress and return later.  

**Priority**: MVP

### User Story 2
As a spec author, I want to turn a rough prompt into a structured draft so that I can move from idea to implementable spec quickly.

**Acceptance Criteria**:
- User provides a short description and the system produces a draft with headings and bullet points.  
- Draft includes at least: scope, assumptions, and edge cases.  
- User can edit the generated content before saving.  

**Priority**: MVP

### User Story 3
As a spec author, I want to generate acceptance criteria from requirements so that the work is testable and unambiguous.

**Acceptance Criteria**:
- User selects a requirement and requests acceptance criteria generation.  
- System outputs criteria in a clear, testable format (e.g., Given/When/Then or checklist).  
- User can accept, edit, or delete generated criteria.  

**Priority**: MVP

### User Story 4
As a spec author, I want to record assumptions and open questions so that unknowns are visible and can be resolved early.

**Acceptance Criteria**:
- User can add an assumption or question with a status (open/resolved).  
- Each item can be assigned an owner or noted as “unassigned”.  
- Resolved items remain visible but clearly marked.  

**Priority**: High

### User Story 5
As a spec reviewer, I want to review a spec against a checklist so that I can approve it consistently.

**Acceptance Criteria**:
- Reviewer sees a checklist aligned to the spec sections (scope, constraints, non-goals, acceptance criteria).  
- Reviewer can mark items as pass/fail and leave a comment.  
- System shows an overall review status (needs changes/approved).  

**Priority**: High

### User Story 6
As a spec reviewer, I want to see what changed since the last review so that I can re-approve quickly.

**Acceptance Criteria**:
- Reviewer can view a change summary between versions (added/removed/edited sections).  
- System highlights changes to acceptance criteria separately from narrative text.  
- Reviewer can request changes or approve the new version.  

**Priority**: High

### User Story 7
As a spec author, I want to link requirements to acceptance criteria so that coverage is easy to verify.

**Acceptance Criteria**:
- User can create a link between a requirement and one or more acceptance criteria.  
- System shows a coverage indicator (e.g., “3/5 requirements have criteria”).  
- System flags requirements with zero linked criteria.  

**Priority**: Medium

### User Story 8
As a spec author, I want to export the spec to Markdown so that I can share it in a repository and review it via pull requests.

**Acceptance Criteria**:
- User can export a spec to a single Markdown document.  
- Export includes the vision/problem statement, scope, constraints, and acceptance criteria.  
- Exported Markdown preserves headings and lists in a readable format.  

**Priority**: MVP

### User Story 9
As a spec author, I want to create a shareable read-only link so that stakeholders can view the latest approved version without editing it.

**Acceptance Criteria**:
- When the author clicks “Share”, the system generates a read-only link for the current spec version.  
- Anyone with the link can view the spec content and acceptance criteria but cannot edit any fields.  
- The author can disable the link, and disabled links show an “access revoked” message.  

**Priority**: Medium

### User Story 10
As a spec author, I want the system to flag missing edge cases so that I can reduce implementation surprises.

**Acceptance Criteria**:
- If the “Edge Cases” section is empty, the system shows a clear prompt to add edge cases before export/review.  
- The system suggests at least 3 edge cases based on the spec content (inputs, errors, limits).  
- The user can add a suggestion to the “Edge Cases” section with one click or dismiss it.  

**Priority**: Low

### User Story 11
As a spec reviewer, I want to leave section-specific comments so that the author knows exactly what to change.

**Acceptance Criteria**:
- Reviewer can add a comment attached to a specific section (e.g., Scope, Constraints, Acceptance Criteria).  
- Each comment is saved with author and timestamp and remains visible until resolved.  
- The spec author can mark a comment as resolved after updating the spec.  

**Priority**: Medium

### User Story 12
As a spec author, I want to see which requirements lack acceptance criteria so that I can ensure the spec is fully testable.

**Acceptance Criteria**:
- System displays a list of requirements that have zero linked acceptance criteria.  
- System provides a “Generate criteria” action from the uncovered requirements list.  
- Coverage status updates immediately after criteria are added and linked.  

**Priority**: High
