# Amp Agent Instructions

## Ralph Wiggum Development Philosophy

This project uses the Ralph Wiggum iterative development technique. When working on tasks:

### Core Principles

1. **Iterate until complete** - Don't stop at "good enough". Keep improving until all requirements are met.
2. **Failures are data** - When something fails, analyze why and fix it in the next iteration.
3. **Self-correction** - Review your own work, run tests, check for issues, and fix them.
4. **Persistence wins** - Keep trying different approaches until success.

### Workflow

1. **Orient** - Read specs, requirements, and existing code
2. **Plan** - Identify what needs to be done
3. **Implement** - Make changes
4. **Validate** - Run tests, linters, type checks
5. **Fix** - Address any failures
6. **Repeat** - Continue until all checks pass

### Validation Commands

Run these after making changes:
```bash
# Syntax check
python -m py_compile src/ntnx_mcp/*.py src/ntnx_mcp/tools/*.py

# Install dependencies (first time)
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Type checking
mypy src/ntnx_mcp

# Linting
ruff check src/ntnx_mcp
```

### Completion Criteria

Only consider a task complete when:
- All tests pass
- No type errors
- No linter errors  
- Requirements are fully implemented
- Code follows existing patterns and conventions
